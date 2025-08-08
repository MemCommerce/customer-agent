from uuid import uuid4

from openai import OpenAI
from agents import Agent, Runner
from agents.mcp import MCPServer
from agents.model_settings import ModelSettings

from schemas import ChatResponse, ChatRequest, MessageResponse, Review, ReviewSentiment
from warranty_info import get_terms_and_conditions, get_default_terms_and_conditions
from mongo_db import db
from mongo_db_session import MongoDBSession


claim_agent = Agent(
    name="Claim specialist agent",
    instructions="""
You are a Claims Specialist Agent for an e-commerce platform. Your role is to assist customers with **returns and warranty claims** for products they have purchased.

Use the tools provided to retrieve brand-specific or default return and warranty terms when helping the customer.

Follow these steps:

1. **Identify the product brand** and type from the user's message.
2. Use `get_terms_and_conditions(brand)` to look up the brand-specific return and warranty policy.
3. If no brand-specific policy is available, use `get_default_terms_and_conditions()` to respond with the default terms.
4. **Clearly explain to the user** the return eligibility, time window, conditions, and any responsibilities (e.g., who covers return shipping).
5. Be friendly, concise, and professional. Avoid legal jargon.
6. Do not guess or invent policies — always use the provided tools to fetch verified information.
7. If the request involves multiple products, handle each one individually.
8. Never disclose internal system details (e.g., tool names or code) to the user.

You are here to help the customer understand what their options are and what steps they need to take.
    """,
    tools=[get_terms_and_conditions, get_default_terms_and_conditions],
)


async def process_message(
    mcp_server: MCPServer, chat_req: ChatRequest, token: str | None = None
) -> ChatResponse:
    instructions = (
        f"""
        You are an E-commerce customer assistant. Use the provided tools to 
        help to human e-commerce customer. Does not answer to non related
        to e-commerce questions. Be grateful. You can answer to greeting 
        messages and similar. 

        Use the provided token for authentication - {token}
    """
        if token
        else """
        You are an E-commerce customer assistant. Use the provided tools to 
        help to human e-commerce customer. Does not answer to non related
        to e-commerce questions. Be grateful. You can answer to greeting 
        messages and similar.
    """
    )
    agent = Agent(
        name="E-commerce Customer Assistant",
        instructions=instructions,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
        tools=[get_terms_and_conditions, get_default_terms_and_conditions],
    )
    conversation_id = (
        chat_req.conversation_id if chat_req.conversation_id else str(uuid4())
    )

    session = MongoDBSession(conversation_id, db)

    print("items")
    print(await session.get_items())

    result = await Runner.run(
        starting_agent=agent, input=chat_req.message, session=session
    )

    output = result.final_output

    return ChatResponse(
        messages=[MessageResponse(content=output)], conversation_id=conversation_id
    )


async def process_review( review: Review):
    prompt = f"""
    Analyze the following product review and return a JSON object with these fields:
    - sentiment: Overall sentiment as one of 'very positive', 'positive', 'neutral', 'negative', 'very negative'.
    - tags: List of up to 3 main topics or issues (e.g., ['shipping', 'quality', 'customer_service']).
    -     aspect_sentiment: dict[str, str]  # Maps aspect (like 'shipping', 'quality') to its sentiment (e.g., {{'shipping': 'positive', 'quality': 'negative'}}).

    Review rating (1-5): {review.rating}
    Review title: {review.title}
    Review content: {review.content}
    Return JSON only.
    """
    client = OpenAI()

    response = client.responses.parse(
        model="gpt-4o",
        input=[
            {
                "role": "system",
                "content": prompt,
            },
        ],
        text_format=ReviewSentiment,
    )

    review_sentiment = response.output_parsed
    if not review_sentiment:
        raise Exception()
    print(review_sentiment)

    review_with_sentiment = Review(
        id=review.id,
        rating=review.rating,
        title=review.title,
        content=review.content,
        product_variant_id=review.product_variant_id,
        order_item_id=review.order_item_id,
        user_id=review.user_id,
        tags=review_sentiment.tags,
        sentiment=review_sentiment.sentiment,
        aspect_sentiment=review_sentiment.aspect_sentiment,
    )

async def process_review_agentic(mcp_server: MCPServer, review: Review):
    instructions = """
    Analyze the provided product review and create these new fields:
    - sentiment: Overall sentiment as one of 'very positive', 'positive', 'neutral', 'negative', 'very negative'.
    - tags: List of up to 3 main topics or issues (e.g., ['shipping', 'quality', 'customer_service']).
    - aspect_sentiment: dict[str, str]  # Maps aspect (like 'shipping', 'quality') to its sentiment (e.g., {{'shipping': 'positive', 'quality': 'negative'}}).

    Use the provided Model Context Protocol tools to add the new fields for Review, using 
    add_sentiment_to_review tool. 

    If the sentiment is very positive or positive, send a personalized thank you to the customer.
    Again use MCP tools for that.
    """
    
    message = f"""
    Review id: {review.id}
    Review rating (1-5): {review.rating}
    Review title: {review.title}
    Review content: {review.content}
    Review product_variant_id: {review.product_variant_id}
    Review order_item_id: {review.order_item_id}
    Review user_id: {review.user_id}

    """

    agent = Agent(
        name="E-commerce product reviews agent",
        instructions=instructions,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
    )

    result = await Runner.run(
        starting_agent=agent, input=message
    )

    output = result.final_output

    print(output)

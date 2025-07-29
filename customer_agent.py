from uuid import uuid4

from agents import Agent, Runner
from agents.mcp import MCPServer
from agents.model_settings import ModelSettings

from schemas import ChatResponse, ChatRequest, MessageResponse
from memory import conversation_store
from warranty_info import get_terms_and_conditions, get_default_terms_and_conditions


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


async def process_message(mcp_server: MCPServer, chat_req: ChatRequest) -> ChatResponse:
    agent = Agent(
        name="E-commerce Customer Assistant",
        instructions="""
        You are an E-commerce customer assistant. Use the provided tools to 
        help to human e-commerce customer. Does not answer to non related
        to e-commerce questions. Be grateful. You can answer to greeting 
        messages and similar. For terms and conditions contact Claims agent.
        """,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
        handoffs=[claim_agent],
    )
    is_new = (
        not chat_req.conversation_id
        or conversation_store.get(chat_req.conversation_id) is None
    )

    if is_new:
        conversation_id: str = uuid4().hex
        state = []
    else:
        conversation_id = chat_req.conversation_id  # type: ignore
        state = conversation_store.get(conversation_id)

    result = await Runner.run(
        starting_agent=agent, input=chat_req.message, context=state
    )
    output = result.final_output
    state.append({"role": "user", "content": chat_req.message})
    state.append({"role": "assistant", "content": output})

    conversation_store.save(conversation_id, state)

    return ChatResponse(
        messages=[MessageResponse(content=output)], conversation_id=conversation_id
    )


async def process_message_with_token(
    mcp_server: MCPServer, chat_req: ChatRequest, token: str
) -> ChatResponse:
    agent = Agent(
        name="E-commerce Customer Assistant",
        instructions=f"""
        You are an E-commerce customer assistant. Use the provided tools to 
        help to human e-commerce customer. Does not answer to non related
        to e-commerce questions. Be grateful. You can answer to greeting 
        messages and similar. 

        Use the provided token for authentication - {token}
        """,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
        tools=[get_terms_and_conditions],
    )
    is_new = (
        not chat_req.conversation_id
        or conversation_store.get(chat_req.conversation_id) is None
    )

    if is_new:
        conversation_id: str = uuid4().hex
        state = []
    else:
        conversation_id = chat_req.conversation_id  # type: ignore
        state = conversation_store.get(conversation_id)

    result = await Runner.run(
        starting_agent=agent, input=chat_req.message, context=state
    )
    output = result.final_output
    state.append({"role": "user", "content": chat_req.message})
    state.append({"role": "assistant", "content": output})

    conversation_store.save(conversation_id, state)

    return ChatResponse(
        messages=[MessageResponse(content=output)], conversation_id=conversation_id
    )

from uuid import uuid4

from agents import Agent, Runner
from agents.mcp import MCPServer
from agents.model_settings import ModelSettings

from schemas import ChatResponse, ChatRequest, MessageResponse
from memory import conversation_store


async def process_message(mcp_server: MCPServer, chat_req: ChatRequest) -> ChatResponse:
    agent = Agent(
        name="E-commerce Customer Assistant",
        instructions="""
        You are an E-commerce customer assistant. Use the provided tools to 
        help to human e-commerce customer. Does not answer to non related
        to e-commerce questions. Be grateful. You can answer to greeting 
        messages and similar.
        """,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
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


async def process_message_with_token(mcp_server: MCPServer, chat_req: ChatRequest, token: str) -> ChatResponse:
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
                                     
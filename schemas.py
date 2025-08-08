from typing import Optional, List, Dict

from pydantic import BaseModel


class MessageResponse(BaseModel):
    content: str


class ChatResponse(BaseModel):
    messages: list[MessageResponse]
    conversation_id: str


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str


class ReviewSentiment(BaseModel):
    sentiment: str
    tags: List[str]
    aspect_sentiment: Dict[str, str] | None = None


class Review(BaseModel):
    id: str
    rating: int
    title: str | None = None
    content: str | None = None

    sentiment: str | None = None
    tags: list[str] | None = None
    aspect_sentiment: dict[str, str] | None = None

    product_variant_id: str
    order_item_id: str
    user_id: str

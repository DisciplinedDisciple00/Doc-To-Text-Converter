from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    model : str = "gpt-oss:20b"

class ChatResponse(BaseModel):
    answer: str
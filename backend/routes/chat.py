from fastapi import APIRouter
from backend.models.chat import ChatRequest, ChatResponse
from backend.services.ask_rag import ask_rag

#Initializing router
router = APIRouter()

#Chat part
@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask_rag(request.message)

    return ChatResponse(answer=answer)
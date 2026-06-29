from fastapi import APIRouter
from backend.models.chat import ChatRequest, ChatResponse
from backend.services.ask_rag import ask_rag
from fastapi.responses import StreamingResponse


#Initializing router
router = APIRouter()

#Chat part
@router.post("/chat")
def chat(request: ChatRequest):
    stream = ask_rag(request.message, request.model)

    return StreamingResponse(
        stream,
        media_type="text/plain"
    )
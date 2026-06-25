from fastapi import APIRouter, UploadFile, File, Form
from backend.services.prepare_rag import prep_rag
from backend.services.text_extraction import text_extraction


upload_router = APIRouter()

@upload_router.post("/upload")
async def upload(file: UploadFile = File(...), start: int = Form(...), end: int = Form(...)):
    targets = (start, end)
    file_bytes = await file.read()
    result = text_extraction(file_bytes, targets)
    prep_rag(result)

    return result
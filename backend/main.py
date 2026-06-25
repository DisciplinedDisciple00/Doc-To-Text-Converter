from fastapi import FastAPI
from backend.routes.chat import router
from backend.routes.upload import upload_router


#Initializing backend server
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}
app.include_router(router)
app.include_router(upload_router)
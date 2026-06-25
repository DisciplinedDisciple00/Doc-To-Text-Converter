from fastapi import FastAPI
from backend.routes.chat import router


#Initializing backend server
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}
app.include_router(router)
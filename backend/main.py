from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router


app = FastAPI(
    title="Cynbit AI Opportunity Assistant",
    description="RAG-based AI assistant for Cynbit",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Cynbit AI Assistant API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# FastAPI entrypoint for MedLama AI/ML service (local only)
from fastapi import FastAPI
from api.routes import chat, auth

# Create FastAPI app
app = FastAPI()

# Include chat and auth routes (local endpoints)
app.include_router(chat.router)
app.include_router(auth.router)

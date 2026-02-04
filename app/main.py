# FastAPI setup
from fastapi import FastAPI
from app.routers.invitation import router as invitation_router

# Initialize FastAPI
app = FastAPI(title="Digital Invitation API")

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Digital Invitation API is running"    }

# Invitation router
app.include_router(invitation_router)

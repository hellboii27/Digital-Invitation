# Main application file
from fastapi import FastAPI
from app.routers.invitation import router as invitation_router
from app.database.init_db import init_db

# Create FastAPI instance
app = FastAPI(title="Digital Invitation API")

# Database initialization
@app.on_event("startup")
def on_startup():
    init_db()

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Digital Invitation API is running"
    }

# Include invitation router
app.include_router(invitation_router)

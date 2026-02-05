# Main application file
from fastapi import FastAPI
from app.routers.invitation import router as invitation_router
from app.database.init_db import init_db

# OpenAPI tags metadata
tags_metadata = [
    {
        "name": "System",
    }
]

# Create FastAPI instance
app = FastAPI(
    title="Digital Invitation API",
    description="""
Backend API untuk sistem Undangan Digital.

👤 **Author**: Bayu Wicaksono  
📦 **Project**: Digital Invitation System  
""",
    version="1.0.0",
    contact={
        "name": "Bayu Wicaksono",
        "email": "b.wicaksono18@gmail.com",
        "url": "https://github.com/hellboii27"
    },
    openapi_tags=tags_metadata
)

# Database initialization
@app.on_event("startup")
def on_startup():
    init_db()

# Root endpoint
@app.get(
    "/",
    tags=["System"],
    summary="Root Endpoint",
    description="Main endpoint for the Digital Invitation API."
)
async def root():
    return {
        "app": "Digital Invitation API",
        "version": "1.0.0",
        "status": "running",
        "docs": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json"
        }
    }

# Health check endpoint
@app.get(
    "/health",
    tags=["System"],
    summary="Health Check",
    description="Endpoint used to verify that the API is running properly."
)
def health_check():
    return {
        "status": "ok",
        "message": "Digital Invitation API is running"
    }

# Include invitation router
app.include_router(invitation_router)

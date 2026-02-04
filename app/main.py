# Main application file
from fastapi import FastAPI
from app.routers.invitation import router as invitation_router
from app.database.init_db import init_db

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
    }
)

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

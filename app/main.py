# FastAPI setup
from fastapi import FastAPI

# Initialize FastAPI
app = FastAPI(title="Digital Invitation API")

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Digital Invitation API is running"    }
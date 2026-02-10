# digitalenv/app/main.py
from fastapi import FastAPI

# Importing schemas
from app.schemas.invitation import InvitationCreate

# API metadata
tags_metadata = [
    {
        "name": "system",
    }
]

# FastAPI application instance
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

# Root endpoint
@app.get(
    "/",
    tags=["system"],
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

# Function to determine guest category based on slug
def kategoriTamu(slug: str):
    pecah=slug.split("-")
    kategori=pecah[0]
    if kategori=="vip":
        return {
            "kode-tamu": pecah[1],
            "Kategori": "VIP"
        }
    elif kategori=="reg":
        return {
            "kode-tamu": pecah[1],
            "Kategori": "Regular"
        }
    else:
        return {
            "kode-tamu": pecah[1],
            "Kategori": "Unknown"
        }

# Invitation endpoint
@app.get("/invitation/{slug}")
def get_invitation(slug: str):
    return kategoriTamu(slug)

# Invitations endpoint with query parameters
@app.get("/invitations")
def get_invitations(limit: int = 10, published: bool = True):
    return {
        "limit": limit,
        "published": published
    }

# Endpoint to create a new invitation
@app.post("/invitations")
def create_invitation(invitation: InvitationCreate):
    return {
        "title": invitation.title,
        "event_date": invitation.event_date,
        "location": invitation.location,
        "description": invitation.description,
        "is_public": invitation.is_public
    }

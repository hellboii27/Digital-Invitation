# Skema untuk undangan digital
from pydantic import BaseModel, Field
from datetime import datetime

# Skema untuk pembuatan undangan
class InvitationCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    event_date: str
    location: str
    description: str | None = None
    is_public: bool = True

# Skema untuk respons undangan
class InvitationResponse(BaseModel):
    title: str
    event_date: str
    location: str
    description: str | None
    is_public: bool = True
    slug: str

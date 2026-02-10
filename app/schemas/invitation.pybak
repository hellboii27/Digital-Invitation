# Skema untuk undangan digital
from pydantic import BaseModel, Field
from datetime import datetime

# Skema untuk pembuatan undangan
class InvitationCreate(BaseModel):
    title: str = Field(..., min_length=3)
    event_date: datetime
    location: str
    description: str | None = None

# Skema untuk respons undangan
class InvitationResponse(BaseModel):
    title: str
    event_date: datetime
    location: str
    description: str | None
    slug: str

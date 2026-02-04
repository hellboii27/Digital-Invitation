# Schemas for invitation creation and response
from pydantic import BaseModel, Field
from datetime import datetime

# Schema for creating a new invitation
class InvitationCreate(BaseModel):
    title: str = Field(..., min_length=3)
    event_date: datetime
    location: str
    description: str | None = None

# Schema for invitation response
class InvitationResponse(BaseModel):
    title: str
    event_date: datetime
    location: str
    description: str | None
    slug: str

# Invitation model
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# Invitation model definition
class Invitation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    slug: str = Field(index=True, unique=True)
    event_date: datetime
    location: str
    description: Optional[str] = None

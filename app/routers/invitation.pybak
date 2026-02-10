# Invitation router
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.schemas.invitation import InvitationCreate, InvitationResponse
from app.models.invitation import Invitation
from app.database.session import get_session
import re

# Define the router
router = APIRouter(prefix="/invitations", tags=["Invitations"])

# Utility function to generate slug from title
def generate_slug(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")

# Endpoint to create a new invitation
@router.post("", response_model=InvitationResponse)
def create_invitation(
    data: InvitationCreate,
    session: Session = Depends(get_session)
):
    slug = generate_slug(data.title)

    exists = session.exec(
        select(Invitation).where(Invitation.slug == slug)
    ).first()

    if exists:
        raise HTTPException(status_code=400, detail="Invitation already exists")

    invitation = Invitation(
        title=data.title,
        slug=slug,
        event_date=data.event_date,
        location=data.location,
        description=data.description
    )

    session.add(invitation)
    session.commit()
    session.refresh(invitation)

    return invitation

# Endpoint to get an invitation by slug
@router.get("/{slug}", response_model=InvitationResponse)
def get_invitation(
    slug: str,
    session: Session = Depends(get_session)
):
    invitation = session.exec(
        select(Invitation).where(Invitation.slug == slug)
    ).first()

    if not invitation:
        raise HTTPException(status_code=404, detail="Invitation not found")

    return invitation

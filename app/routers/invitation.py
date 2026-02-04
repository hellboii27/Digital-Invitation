# Router untuk mengelola undangan digital
from fastapi import APIRouter, HTTPException
from app.schemas.invitation import InvitationCreate, InvitationResponse
import re

router = APIRouter(prefix="/invitations", tags=["Invitations"])

# Simulasi database (sementara)
FAKE_DB = {}

# Fungsi untuk membuat slug dari judul undangan
def generate_slug(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")

# Endpoint untuk membuat undangan baru
@router.post("", response_model=InvitationResponse)
def create_invitation(data: InvitationCreate):
    slug = generate_slug(data.title)

    if slug in FAKE_DB:
        raise HTTPException(status_code=400, detail="Invitation already exists")

    invitation = {
        "title": data.title,
        "event_date": data.event_date,
        "location": data.location,
        "description": data.description,
        "slug": slug
    }

    FAKE_DB[slug] = invitation
    return invitation

# Endpoint untuk mendapatkan undangan berdasarkan slug
@router.get("/{slug}", response_model=InvitationResponse)
def get_invitation(slug: str):
    invitation = FAKE_DB.get(slug)

    if not invitation:
        raise HTTPException(status_code=404, detail="Invitation not found")

    return invitation

# Database initialization
from sqlmodel import SQLModel
from app.database.session import engine
from app.models.invitation import Invitation

# Function to initialize the database
def init_db():
    SQLModel.metadata.create_all(engine)

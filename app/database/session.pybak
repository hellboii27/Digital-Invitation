# Database session setup
from sqlmodel import SQLModel, create_engine, Session

# SQLite database URL
DATABASE_URL = "sqlite:///./invitation.db"

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

# Create all tables in the database
def get_session():
    with Session(engine) as session:
        yield session

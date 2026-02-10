# digitalenv/app/main.py
from fastapi import FastAPI

# from pydantic import BaseModel
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello world!"}

# Users endpoints
@app.get("/users")
def get_users():
    return [
    {"id": 1, "name": "Andi"},
    {"id": 2, "name": "Budi"}
    ]

# Endpoint to get a specific user by name
@app.get("/users/{user}")
def get_user(user: str):
    return {"name": user}

#   Schema for user creation
class User(BaseModel):
    name: str
    email: str

# Endpoint to create a new user
@app.post("/users")
def create_user(userdata: User):
    return userdata

# Schema for product creation
class create_product(BaseModel):
    id: int
    name: str
    price: float

# Products endpoints
@app.get("/products")
def get_products():
    return [
    {"id": 1, "name": "Sabun", "price": "Rp 5.000"},
    {"id": 2, "name": "Sampo", "price": "Rp 2.000"}
    ]

# Endpoint to create a new product
@app.post("/products")
def create_product(product: create_product):
    return product

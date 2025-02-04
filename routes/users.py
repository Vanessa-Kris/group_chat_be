from fastapi import APIRouter, HTTPException
from models import User
from schemas import UserCreate, UserResponse
import uuid
import random

router = APIRouter()

ADJECTIVES = ["Mysterious", "Quiet", "Brave", "Witty", "Gentle"]
NOUNS = ["Fox", "Shadow", "Falcon", "Panda", "Seeker"]

def generate_random_name():
    return f"{random.choice(ADJECTIVES)}{random.choice(NOUNS)}{random.randint(1000, 9999)}"

@router.post("/users/", response_model=UserResponse)
def create_user(user_data: UserCreate):
    random_name = generate_random_name()
    try:
        user = User.create(random_name=random_name, session_id=user_data.session_id)
        return {"id": user.id, "random_name": user.random_name}
    except:
        raise HTTPException(status_code=400, detail="Session ID already exists")

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    session_id: str

class UserResponse(BaseModel):
    id: int
    random_name: str

class PostCreate(BaseModel):
    user_id: int
    content: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: str

class ReplyCreate(BaseModel):
    post_id: int
    user_id: int
    content: str

class ReplyResponse(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    created_at: str

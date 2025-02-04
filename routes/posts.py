from fastapi import APIRouter, HTTPException
from models import Post, User
from schemas import PostCreate, PostResponse
from datetime import datetime

router = APIRouter()

@router.post("/posts/", response_model=PostResponse)
def create_post(post_data: PostCreate):
    user = User.get_or_none(id=post_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    post = Post.create(user=user, content=post_data.content, created_at=datetime.utcnow())
    return {"id": post.id, "user_id": post.user.id, "content": post.content, "created_at": str(post.created_at)}

@router.get("/posts/")
def get_posts():
    return [{"id": p.id, "user_id": p.user.id, "content": p.content, "created_at": str(p.created_at)} for p in Post.select()]

from fastapi import APIRouter, HTTPException
from models import Reply, Post, User
from schemas import ReplyCreate, ReplyResponse
from datetime import datetime

router = APIRouter()

@router.post("/replies/", response_model=ReplyResponse)
def create_reply(reply_data: ReplyCreate):
    post = Post.get_or_none(id=reply_data.post_id)
    user = User.get_or_none(id=reply_data.user_id)

    if not post or not user:
        raise HTTPException(status_code=404, detail="Post or User not found")

    reply = Reply.create(post=post, user=user, content=reply_data.content, created_at=datetime.utcnow())
    return {"id": reply.id, "post_id": reply.post.id, "user_id": reply.user.id, "content": reply.content, "created_at": str(reply.created_at)}

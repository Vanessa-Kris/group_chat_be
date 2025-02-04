from fastapi import FastAPI
from db import init_db
from routes import users, posts, replies

app = FastAPI()

# Initialize the database
init_db()

# Include routes
app.include_router(users.router, prefix="/api")
app.include_router(posts.router, prefix="/api")
app.include_router(replies.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Anonymous Forum API"}

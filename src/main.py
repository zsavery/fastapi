from random import randrange
from typing import Optional
from fastapi import  FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = [{"title": "title of post1", "content": "content of post 1", "id": 1},
           {"title": "favorite foods", "content": " Pizza", "id": 2}]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 10000000)
    my_post.append(post_dict)
    return {"data": post_dict}




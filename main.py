from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/post")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(newpost: Post):
    print(newpost.published)
    return {"data": "newpost"}


# title str, content str

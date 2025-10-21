from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn



app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blog posts from the db'}
    else:
        return {'data': f'{limit} blog posts from the db'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blog'}


@app.get("/blog/{id}")
def show(id: int):
    return {'data': id}



@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": f"all comments for blog {id}"}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create(blog: Blog):
    return {"data": f"blog post created {blog.title}"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
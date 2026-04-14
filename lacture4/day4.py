from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request ke liye (client se kya aayega)
class NewPost(BaseModel):
    title: str
    content: str

# response / internal use ke liye (id ke sath)
class Post(NewPost):
    id: int


my_posts = [
    {'id': 1, 'title': 'first post', 'content': 'this is the first post'},
    {'id': 2, 'title': 'second post', 'content': 'this is the second post'},
]

# GET (yaha body nahi hoti)
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# POST
@app.post("/createposts")
def create_posts(post: NewPost):
    post_dict = post.dict()
    post_dict["id"] = len(my_posts) + 1
    my_posts.append(post_dict)
    return {"data": post_dict}

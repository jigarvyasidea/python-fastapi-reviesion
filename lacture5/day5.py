from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content:str

my_posts = [
    {"id": 1 , "title": "first post", "content": "this is the first post content"},
    {"id": 2 , "title": "second post", "content": "this is the second post content"},

]



@app.get("/")
def get_post():
    for i in my_posts:
        logger.debug(f"Post ID: {i['id']} , Title: {i['title']} , Content: {i['content']}")

    return {"message": my_posts}


# lets focus on task 2 

# now i need to create post post create kanra ke liye we need to save that post in aray so need to wirte psot requet

@app.post("/createpost")
def create_post(post: Post):
    logger.info(f"Creating post with title: {post.title} and content: {post.content}")
    # now we need to save post in the dict so 
    post.id = len(my_posts) + 1
    logger.info(f"Assigned ID {post.id} to the new post")
    my_posts.append(post.dict())
    
    return {"message": "post created successfully" , "post": post}


# now we need to dispaly signle post by ID
@app.get("/getpost/{id}")
def get_single_post(id:int):
    logger.info(f"fetching post with id {id}")
    for i in my_posts:
        if i['id'] == id:
            logger.info(f"post found: {i}")
            return {"message": i}
    logger.warning(f"post with id {id} not found")

#task2 need to add validation for that need to use pydantic 
# task 1 get all the post 
# task 2 create post 
# task 3 :- get single post by id 
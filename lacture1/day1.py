from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# we need to create one Hope api so 


@app.get("/")
async def home_ui():
    return {"message": "Welcome to FastAPI"}


# let create one more api 

@app.get("/posts")
async def get_posts():
    return {"message": "Here are all the posts"}




@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    # it pake that data from dict of body then put all data into paylaod 
    print(payLoad)
    return {"new_posts" : f" title {payLoad  ['title']} and content {payLoad['content']}  and content : {payLoad['content']} created successfully   "}



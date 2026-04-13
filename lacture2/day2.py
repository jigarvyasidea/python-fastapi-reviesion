from fastapi import FastAPI
from fastapi.params import Body 

app = FastAPI()




@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    # it pake that data from dict of body then put all data into paylaod 
    print(payLoad)
    return {"new_posts" : f" title {payLoad  ['title']} and content {payLoad['content']}  and content : {payLoad['content']} created successfully   "}




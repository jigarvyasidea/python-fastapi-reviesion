from fastapi import FastAPI 
from fastapi.params import Body 

from pydantic import BaseModel 



# now i wnat to validate api that title and conteact must bestru for that what i do is  

class new_post(BaseModel):
    title:str
    content:str


app = FastAPI()


@app.get("/")
def home_ui():
    return {"message": "Welcome to FastAPI"}

@app.post("/createposts")
def create_posts(new_posts: new_post):
    # now we  want to print that title and content 

    print(new_posts.title)

    print(new_posts.content)

    return {"message" : "post is created successfully"} 



# now i wnatr to contect i am seing that visible and pritnt there for that all come in payload 

# firdt we extract alp that from body and they put into pydantic 


# now let used pydancitc oin tist 

# how pydacnic help us to vlaidaite the data in api it its not validaiteit show the erorr in deprpate libiary 
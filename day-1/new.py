from fastapi import FastAPI

app = FastAPI()

# now i wnat to create home apth so 

@app.get("/")
def home_ui():
    return "Welcome to Golden eagle "


# now i want to create contact us raoute so 


@app.get("/contact")
def contact_us():
    return "contact us page" 

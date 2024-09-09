from fastapi import FastAPI
from models import User



app = FastAPI()


user_list = []

@app.get('/')
def init():
    return {"data":"Hello World"}

@app.post('/add/user/')
def add_user(user:User):
    
    user_list.append(user)

    return {
        "Status":"ok",
        "data":user_list
        }
    

@app.get('/user/')
def get_user():
    return {"data":user_list}

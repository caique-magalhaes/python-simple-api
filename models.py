from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    drive_license:bool
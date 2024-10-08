from fastapi import FastAPI
from pydantic import EmailStr , BaseModel
from typing import Optional

app = FastAPI()

employes = {
    1: {
        "name": "Muhammad Awais Qamar",
        "age": 22,
        "email": "awaisqamar@gmail.com",
        "department": "Computer Science",
    }
}

class Employe(BaseModel):
    name: str
    age: int
    email: EmailStr
    department: str

class EmployeUpdate(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[EmailStr] = None
    department : Optional[str] = None

@app.get("/")
def index():
    return {"Employee": "Enter the Employee Data"}

@app.get("/get-employe/{employe_id}")
def get_employe(employe_id: int):
    if employe_id in employes:
        return employes[employe_id]
    else:
        return ("Employe ID Deleted Successfully")

@app.post("/create-employe/{employe_id}")
def create_employe(employe_id: int , employe: Employe):
    if employe_id in employes:
        return{"Message": "Empolye exits"}
    
    employes[employe_id] = employe
    return employes[employe_id]

@app.put("/update-employe/{employe_id}")
def update_employe(employe_id: int , employe: EmployeUpdate):
    if employe_id not in employes:
        return {"Message": "Employe Data Does Not Exit"}
    
    if employe.name != None:
        employes[employe_id].name = employe.name
    
    if employe.age != None:
        employes[employe_id].age = employe.age
    
    if employe.email != None:
        employes[employe_id].email = employe.email
    
    if employe.department != None:
        employes[employe_id].department = employe.department
    
    employes[employe_id]  = employe
    return employes[employe_id]

@app.delete("/delete-employe/{employe_id}")
def delete_employe(employe_id : int):
    if employe_id not in employes:
        return {"Error" : "Employe Data Does Exit"}
    
    del employes[employe_id]
    return {"Message": "Employe Sucessfully Delete"}



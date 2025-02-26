# from fastapi import FastAPI , Path
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# students = {
#     1: {
#         "name": "Muhammad Awais",
#         "age": 22,
#         "year": "Year 12",
#     }
# }

# class Student(BaseModel):
#     name : str
#     age : int
#     year : str

# # Upadte Part
# class UpdateStudent(BaseModel):
#     name:  Optional[str] = None
#     age:  Optional[int] = None
#     year: Optional[str] = None


# @app.get("/")
# def index():
#     return {"name": "First Data"}
  
# # @app.get("/get-student/{student_id}")
# # def get_student(student_id: int = Path(None , description = "The ID of the student you went to view",gt=0,lt=3)):
# #     return students[student_id]

# @app.get("/get-by-name/{student_id}")
# def get_student(*, student_id: int, name: Optional[str] = None , test : int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not found"}

# @app.post("/create-student/{student_id}")
# def create_student(student_id : int , student : Student):
#     if student_id in students:
#         return("Error" , "Students exists")
#     students[student_id] = student
#     return students[student_id]

# #Update Part

# @app.put("/update_student/{student_id}")
# def update_student(student_id: int , student: UpdateStudent):
#     if student_id not in students:
#         return {"Error" , "Student does not exits"}
    
#     if student.name != None:
#         students[student_id].name = student.name
    
#     if student.age != None:
#         students[student_id].age = student.age
    
#     if student.year != None:
#         students[student_id].year = student.year

#     # students[student_id] = student
#     return students[student_id]


# #Delete Part
# @app.delete("/delete_student/{student_id}")
# def delete_student(student_id: int , student):
#     if student_id not in students:
#         return {"Error": "Student Does not exits"}
    
#     del students[student_id]
#     return {"Message": "Student Deleted Successfully"}



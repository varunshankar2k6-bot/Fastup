from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
app = FastAPI()
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}
@app.post("/student")
def create_student(student: dict):
    return {
        "name": student["name"],
        "course": student["course"]
    }
class Address(BaseModel):
    city: str
    state: str
class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=18, lt=100)
    course: str
    email: Optional[EmailStr] = None
    address: Address
    courses: list[str]
@app.post("/students")
def create_students(student: Student):
    return student
@app.post("/student/{course_id}")
def create_student_with_id(course_id: int, student: Student):
    return {
        "course_id": course_id,
        "student": student
    }
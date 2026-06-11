from fastapi import FastAPI
from models.student import Student

app = FastAPI()


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


@app.post("/student")
def create_student(student: Student):
    return student


@app.post("/student/{course_id}")
def create_student_with_id(course_id: int, student: Student):
    return {
        "course_id": course_id,
        "student": student
    }
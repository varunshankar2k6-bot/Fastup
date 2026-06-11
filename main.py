from fastapi import FastAPI
from models.student import Student, StudentResponse
app = FastAPI()
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

#Post
@app.post("/student", response_model=StudentResponse)
def create_student(student: Student):
    return {
        "id": 101,
        **student.model_dump()
    }

#Get
@app.get("/student/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):

    student = {
        "id": student_id,
        "name": "John",
        "age": 20,
        "course": "Python",
        "email": "john@gmail.com"
    }

    return student


# PUT
@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    return {
        "message": "Student updated successfully",
        "student": {
            "id": student_id,
            **student.model_dump()
        }
    }


# DELETE
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
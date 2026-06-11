from pydantic import BaseModel, EmailStr
from typing import Optional
class Address(BaseModel):
    city: str
    state: str
class Student(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[EmailStr] = None
    address: Address
    courses: list[str]
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: Optional[EmailStr] = None
    address: Address
    courses: list[str]
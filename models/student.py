from pydantic import BaseModel, Field, EmailStr
from typing import Optional

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
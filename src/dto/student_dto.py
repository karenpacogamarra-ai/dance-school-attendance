from pydantic import BaseModel


class StudentCreate(BaseModel):
        name: str
        surname: str
        age: int


class Student (BaseModel):
        id: str
        name: str
        surname: str
        age: int


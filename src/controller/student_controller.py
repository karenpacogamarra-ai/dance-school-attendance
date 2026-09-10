from dto.student_dto import Student, StudentCreate
from fastapi import APIRouter
import uuid 

router = APIRouter()
students = []


@router.post("/students/")
def create_student(student: StudentCreate):

    if len(student.name) > 2:
        print('Guardado')
        student_c = Student(
            id = str(uuid.uuid4()),
            name = student.name,
            surname = student.surname,
            age = student.age
        )
        students.append(student_c)
        return student_c
    else:
        print('tu estas mal, todo el maldito mundo esta mal')


@router.get("/students/")
def get_student():
        return students


@router.get("/students/{id}")
def get_student_ID(id: str):
    for student in students:
        if student.id == id:
            return student
    
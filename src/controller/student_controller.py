from dto.student_dto import StudentCreate
from fastapi import APIRouter, Depends
from service.student_service import StudentService

router = APIRouter()
students = []

def get_student_services():
    return StudentService(students)


@router.post("/students/")
def create_student(student: StudentCreate, student_service = Depends(get_student_services)):
    return student_service.create(student)
    


@router.get("/students/")
def get_student( student_service = Depends(get_student_services)):
    return student_service.get()


@router.get("/students/{id}")
def get_student_ID(id: str, student_service = Depends(get_student_services)):
    return student_service.get_id(id)
    
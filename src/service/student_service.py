
import uuid

from dto.student_dto import Student, StudentCreate
from repository.student_repository import StudentRepository


class StudentService():

    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def create(self, student_create: StudentCreate):
            if len(student_create.name) > 2:
                print('Guardado')
                student_c = Student(
                    id = str(uuid.uuid4()),
                    name = student_create.name,
                    surname = student_create.surname,
                    age = student_create.age
                )
                self.student_repo.create(student_c)
                return student_c
            else:
                print('tu estas mal, todo el maldito mundo esta mal')

    def get(self):
         return self.student_repo.get()

    def get_id(self, id: str):
        return self.student_repo.get_id(id)
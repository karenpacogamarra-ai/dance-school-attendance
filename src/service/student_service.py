
import uuid

from dto.student_dto import Student, StudentCreate


class StudentService():

    def __init__(self, students):
        self.students = students

    def create(self, student_create: StudentCreate):
            if len(student_create.name) > 2:
                print('Guardado')
                student_c = Student(
                    id = str(uuid.uuid4()),
                    name = student_create.name,
                    surname = student_create.surname,
                    age = student_create.age
                )
                self.students.append(student_c)
                return student_c
            else:
                print('tu estas mal, todo el maldito mundo esta mal')

    def get(self):
         return self.students

    def get_id(self, id: str):
        for student in self.students:
            if student.id == id:
                 return student
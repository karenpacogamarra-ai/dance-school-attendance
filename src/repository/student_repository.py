
from dto.student_dto import Student


class StudentRepository():

    def __init__(self, students):
        self.students = students

    def create(self, student: Student):
        self.students.append(student)
        return student

    def get(self):
        return self.students

    def get_id(self, id: str):
        for student in self.students:
            if student.id == id:
                return student

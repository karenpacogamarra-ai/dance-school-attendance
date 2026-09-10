
from dto.dance_class_dto import DanceClass, DanceClassCreate
from fastapi import APIRouter
import uuid 


router = APIRouter()
dance_classes = []

@router.post("/classes/")
def create_class(dance_class: DanceClassCreate):

    if len(dance_class.name) > 2:
        print('Guardado')
        dance_class_h = DanceClass(
            id = str(uuid.uuid4()), 
            name = dance_class.name, 
            level = dance_class.level, 
            start_time = dance_class.start_time, 
            end_time = dance_class.end_time, 
            cost = dance_class.cost )
        
        dance_classes.append(dance_class_h)
        
        return dance_class_h
    
    else:
        print('tu estas mal, todo el maldito mundo esta mal')


@router.get("/classes/")
def get_classes():
    return dance_classes


@router.get("/classes/{id}")
def get_student_ID(id: str):
    for course in dance_classes:
        if course.id == id:
            return course
    
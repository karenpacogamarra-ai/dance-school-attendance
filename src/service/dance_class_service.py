
from dto.dance_class_dto import DanceClass, DanceClassCreate
import uuid


class DanceClassService():

    def __init__(self, dance_classes):
        self.dance_classes = dance_classes
    
    def create(self, dance_class_create: DanceClassCreate):
        if len(dance_class_create.name) > 2:
            print('Guardado')
            dance_class = DanceClass(
                id = str(uuid.uuid4()), 
                name = dance_class_create.name, 
                level = dance_class_create.level, 
                start_time = dance_class_create.start_time, 
                end_time = dance_class_create.end_time, 
                cost = dance_class_create.cost )
            
            self.dance_classes.append(dance_class)
            
            return dance_class
        
        else:
            print('tu estas mal, todo el maldito mundo esta mal')
    
    def get(self):
        return self.dance_classes

    def get_by_id(self, id: str):
        for course in self.dance_classes:
            if course.id == id:
             return course


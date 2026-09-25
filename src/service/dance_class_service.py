
from dto.dance_class_dto import DanceClass, DanceClassCreate
import uuid

from repository.dance_class_repository import DanceClassRepository


class DanceClassService():

    def __init__(self, dance_class_repo: DanceClassRepository):
        self.dance_class_repo = dance_class_repo
    
    def create(self, dance_class_create: DanceClassRepository):
        if len(dance_class_create.name) > 2:
            print('Guardado')
            dance_class = DanceClass(
                id = str(uuid.uuid4()), 
                name = dance_class_create.name, 
                level = dance_class_create.level, 
                start_time = dance_class_create.start_time, 
                end_time = dance_class_create.end_time, 
                cost = dance_class_create.cost )
            
            return self.dance_class_repo.create(dance_class)
        else:
            print('tu estas mal, todo el maldito mundo esta mal')
    
    def get(self):
        return self.dance_class_repo.get()

    def get_by_id(self, id: str):
        return self.dance_class_repo.get_by_id(id)


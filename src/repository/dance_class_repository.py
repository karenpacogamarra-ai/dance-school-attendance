from dto.dance_class_dto import DanceClass


class DanceClassRepository():

    def __init__(self, dance_clases: list):
        self.dance_clases = dance_clases

    def create(self, dance_clase: DanceClass):
        self.dance_clases.append(dance_clase)
        return dance_clase

    def get(self):
        return self.dance_clases

    def get_by_id(self, id: str):
        for dance_clase in self.dance_clases:
            if dance_clase.id == id:
                return dance_clase

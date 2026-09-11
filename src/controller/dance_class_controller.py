
from dto.dance_class_dto import DanceClassCreate
from fastapi import APIRouter, Depends
from service.dance_class_service import DanceClassService


router = APIRouter()
dance_classes = []

def get_dance_class_service():
    return DanceClassService(dance_classes)
    
    

@router.post("/classes/")
def create_class(dance_class: DanceClassCreate, dance_class_service = Depends(get_dance_class_service)):
    return dance_class_service.create(dance_class)

    


@router.get("/classes/")
def get_classes(dance_class_service = Depends(get_dance_class_service)):
    return dance_class_service.get()


@router.get("/classes/{id}")
def get_class_dance_id(id: str, dance_class_service = Depends(get_dance_class_service)):
    return dance_class_service.get_by_id(id)



from pydantic import BaseModel


class DanceClassCreate(BaseModel):
        name: str
        level: str 
        start_time: int
        end_time: int        
        cost: float


class DanceClass(BaseModel):
        id: str
        name: str
        level: str 
        start_time: int
        end_time: int        
        cost: float
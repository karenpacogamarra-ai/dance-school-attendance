from fastapi import FastAPI
from controller.dance_class_controller import router as dance_class_router
from controller.student_controller import router as student_router


app = FastAPI()

app.include_router(dance_class_router)
app.include_router(student_router)




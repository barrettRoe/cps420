
from fastapi import FastAPI, status, APIRouter
from model.rectangle import Rectangle
import fake.rectangle as service

router = APIRouter(prefix = "/rectangle")

@router.get("/")
def top():
   return "top rectangle endpoint"

@router.get("/")
def get_all() -> list[Rectangle]:
    return service.get_all()

@router.get("/{width}}")
def get_one(width) -> Rectangle | None:
    return service.get_one(width)

@router.get("/{height}}")
def get_one(height) -> Rectangle | None:
    return service.get_one(height)

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(rectangle: Rectangle) -> Rectangle:
    return service.create(rectangle)

@router.patch("/")
def modify(rectangle: Rectangle) -> Rectangle:
    return service.modify(rectangle)

@router.put("/")
def replace(rectangle: Rectangle) -> Rectangle:
    return service.replace(rectangle)

@router.delete("/{width}")
def delete(width: float):
    return None

@router.delete("/{height}")
def delete(height: float):
    return None
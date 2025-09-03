# installation de fastapi -> pip install fastapi
# Demarer le serveur -> uvicorn main:app --reload
# STD24002 K4

# pour tester l'API curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Car (BaseModel):
    text: str = None
    is_done: bool =False

cars =[]

@app.get("/ping")
def root():
    return {"pong"}

@app.post("/cars")
def create_cars(new_cars: list[dict]):
    start_id = len(cars) + 1
    for i, t in enumerate(new_cars):
        t["id"] = start_id + i
        cars.append(t)
    return new_cars

@app.get("/cars",response_model=list[Car])
def list_cars(limit: int = 10):
    return cars[0:limit]

@app.get("/cars/{id}")
def get_car(id: int):
    for Car in cars:
        if Car["id"] == id:
            return Car
    raise HTTPException(status_code=404, detail="Car not found")

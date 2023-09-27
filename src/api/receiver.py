from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class WorkoutReceived(BaseModel):
    name: str
    sets: int
    totalRepetitions: int
    maxRepetitions: int
    performances: int
    id: int

class TrainingReceived(BaseModel):
    name: str
    durationMinutes: int
    performances: int
    id: int


app = FastAPI()


@app.post("/workouts/")
async def push_workout(workout: WorkoutReceived):
    pass

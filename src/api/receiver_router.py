import pyodbc
from fastapi import APIRouter, Depends, HTTPException

from src.database.connection import get_database_connection
from src.database.writer.writer import insert
from src.database.writer.queries import *
from src.api.received_objects import *

receiver_router = APIRouter()


@receiver_router.post("/workouts/")
async def push_workout(workout_received: WorkoutReceived, database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        insert(workout_query, workout_received, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Workout added successfully"}

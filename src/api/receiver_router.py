import pyodbc
from fastapi import APIRouter, Depends, HTTPException

from src.database.connection import get_database_connection
from src.database.writer.writer import insert, update
import src.database.writer.queries as query
from src.api.received_objects import *

receiver_router = APIRouter()


@receiver_router.post("/insert_workout/")
async def insert_workout(workout_received: WorkoutReceived, database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        insert(query.insert_workout, workout_received, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Workout inserted successfully"}

@receiver_router.post("/insert_training/")
async def insert_training(training_received: TrainingReceived, database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        insert(query.insert_training, training_received, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Training inserted successfully"}

@receiver_router.post("/update_workout/")
async def update_workout(workout_received: WorkoutReceived, database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        update(query.update_workout, workout_received, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Workout updated successfully"}

@receiver_router.post("/update_training/")
async def update_training(training_received: TrainingReceived, database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        update(query.update_training, training_received, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Training updated successfully"}

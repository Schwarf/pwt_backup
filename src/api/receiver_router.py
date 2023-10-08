import pyodbc
from fastapi import APIRouter, Depends, HTTPException

import src.database.writer.queries as query
from src.api.received_objects import *
from src.database.connection import get_database_connection
from src.database.writer.writer import insert, update

receiver_router = APIRouter()


@receiver_router.post("/insert_workouts/")
async def insert_workout(workouts_received: WorkoutListReceived,
                         database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for workout in workouts_received.workouts:
                insert(query.insert_workout, workout, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in Workouts: {e}")
    return {"status": "Workout inserted successfully"}


@receiver_router.post("/insert_trainings/")
async def insert_training(trainings_received: TrainingListReceived,
                          database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for training in trainings_received.trainings:
            insert(query.insert_training, training, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in Trainings: {e}")
    return {"status": "Training inserted successfully"}


@receiver_router.post("/insert_workout_timestamps/")
async def insert_workout(workout_timestamps_received: WorkoutTimestampListReceived,
                         database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for workout_timestamp in workout_timestamps_received.workout_timestamp:
                insert(query.insert_workout_timestamp, workout_timestamp, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in Workout Timestamps: {e}")
    return {"status": "Workout Timestamp inserted successfully"}


@receiver_router.post("/insert_training_timestamps/")
async def insert_training(training_timestamps_received: TrainingTimestampReceived,
                         database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for training_timestamp in training_timestamps_received.training_timestamp:
                insert(query.insert_training_timestamp, training_timestamp, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in Training Timestamps: {e}")
    return {"status": "Training Timestamp inserted successfully"}


@receiver_router.post("/update_workouts/")
async def update_workout(workouts_received: WorkoutListReceived,
                         database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for workout in workouts_received.workouts:
            update(query.update_workout, workout, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Workout updated successfully"}


@receiver_router.post("/update_trainings")
async def update_training(trainings_received: TrainingListReceived,
                          database: pyodbc.Connection = Depends(get_database_connection)):
    try:
        for training in trainings_received.trainings    :
            update(query.update_training, training, database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")
    return {"status": "Training updated successfully"}

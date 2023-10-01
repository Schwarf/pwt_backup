from typing import Tuple

from src.api.received_objects import WorkoutReceived, TrainingReceived, WorkoutTimestampReceived, \
    TrainingTimestampReceived


def insert_workout(workout_received: WorkoutReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""INSERT INTO {table}(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id, isDeleted) VALUES 
        ('{workout_received.name}', {workout_received.sets}, {workout_received.totalRepetitions}, 
        {workout_received.maxRepetitions}, {workout_received.performances}, {workout_received.id}, {workout_received.isDeleted})"""
    return query, table


def insert_training(training_received: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""INSERT INTO {table}(name, durationMinutes, performances, id, isDeleted) VALUES 
            ('{training_received.name}',{training_received.durationMinutes}, {training_received.performances}, {training_received.id},
            {training_received.isDeleted})"""
    return query, table


def update_training(training_received: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""UPDATE {table} SET name='{training_received.name}', durationMinutes={training_received.durationMinutes}, performances={training_received.performances},
                isDeleted={training_received.isDeleted}
                WHERE id={training_received.id}"""
    return query, table


def update_workout(workout_received: WorkoutReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""UPDATE {table} SET name='{workout_received.name}', sets={workout_received.sets}, totalRepetitions={workout_received.totalRepetitions},
             maxRepetitionsInSet={workout_received.maxRepetitions}, performances={workout_received.performances}, isDeleted={workout_received.isDeleted}
                WHERE id={workout_received.id}"""
    return query, table


def insert_workout_timestamp(workout_timestamp_received: WorkoutTimestampReceived) -> Tuple[str, str]:
    table = "workout_timestamps"
    query = f"""INSERT INTO {table}(id, workoutId, timestamp, isDeleted) VALUES 
        ('{workout_timestamp_received.id}', {workout_timestamp_received.workoutId}, {workout_timestamp_received.timestamp}, {workout_timestamp_received.isDeleted}"""
    return query, table


def insert_training_timestamp(training_timestamp_received: TrainingTimestampReceived) -> Tuple[str, str]:
    table = "training_timestamps"
    query = f"""INSERT INTO {table}(id, trainingId, timestamp, isDeleted) VALUES 
        ('{training_timestamp_received.id}', {training_timestamp_received.trainingId}, {training_timestamp_received.timestamp}, {training_timestamp_received.isDeleted}"""
    return query, table

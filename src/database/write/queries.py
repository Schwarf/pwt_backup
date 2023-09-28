from typing import Tuple

from src.api.receiver import WorkoutReceived, TrainingReceived, WorkoutTimestampReceived, TrainingTimestampReceived


def workout_query(workout_received: WorkoutReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""INSERT INTO {table}(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id) VALUES 
        ('{workout_received.name}', {workout_received.sets}, {workout_received.totalRepetitions}, 
        {workout_received.maxRepetitions}, {workout_received.performances}, {workout_received.id})"""
    return query, table


def training_query(training_received: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""INSERT INTO {table}(name, durationMinutes, performances, id) VALUES 
            ('{training_received.name}',{training_received.durationMinutes}, {training_received.performances}, {training_received.id})"""
    return query, table


def update_training_query(training_received: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""UPDATE {table} SET name='{training_received.name}', durationMinutes={training_received.durationMinutes}, performances={training_received.performances}
                WHERE id={training_received.id}"""
    return query, table


def update_workout_query(workout_received: WorkoutReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""UPDATE {table} SET name='{workout_received.name}', sets={workout_received.sets}, totalRepetitions={workout_received.totalRepetitions},
             maxRepetitionsInSet={workout_received.maxRepetitions}, performances={workout_received.performances}
                WHERE id={workout_received.id}"""
    return query, table


def workout_timestamp_query(workout_timestamp_received: WorkoutTimestampReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""INSERT INTO {table}(id, workoutId, timestamp) VALUES 
        ('{workout_timestamp_received.id}', {workout_timestamp_received.workoutId}, {workout_timestamp_received.timestamp}"""
    return query, table

def training_timestamp_query(training_timestamp_received: TrainingTimestampReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""INSERT INTO {table}(id, trainingId, timestamp) VALUES 
        ('{training_timestamp_received.id}', {training_timestamp_received.trainingId}, {training_timestamp_received.timestamp}"""
    return query, table

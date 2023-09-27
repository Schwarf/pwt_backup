from typing import Tuple

from src.api.receiver import WorkoutReceived, TrainingReceived


def workout_query(workoutReceived: WorkoutReceived) -> Tuple[str, str]:
    table = "workouts"
    query = f"""INSERT INTO {table}(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id) VALUES 
        ('{workoutReceived.name}', {workoutReceived.sets}, {workoutReceived.totalRepetitions}, 
        {workoutReceived.maxRepetitions}, {workoutReceived.performances}, {workoutReceived.id})"""
    return query, table


def training_query(trainingReceived: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""INSERT INTO {table}(name, durationMinutes, performances, id) VALUES 
            ('{trainingReceived.name}',{trainingReceived.durationMinutes}, {trainingReceived.performances}, {trainingReceived.id})"""
    return query, table

def update_training_query(trainingReceived: TrainingReceived) -> Tuple[str, str]:
    table = "trainings"
    query = f"""UPDATE {table} SET name='{trainingReceived.name}', durationMinutes={trainingReceived.durationMinutes}, performances={trainingReceived.performances}
                WHERE id={trainingReceived.id}"""
    return query, table

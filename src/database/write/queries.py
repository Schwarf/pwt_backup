from typing import Tuple

from src.api.receiver import WorkoutReceived, TrainingReceived


def workout_query(workoutReceived: WorkoutReceived) -> Tuple[str, str]:
    query = f"""INSERT INTO workouts(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id) VALUES 
        ('{workoutReceived.name}', {workoutReceived.sets}, {workoutReceived.totalRepetitions}, 
        {workoutReceived.maxRepetitions}, {workoutReceived.performances}, {workoutReceived.id})"""
    table = "workouts"
    return query, table


def training_query(trainingReceived: TrainingReceived) -> Tuple[str, str]:
    query = f"""INSERT INTO trainings(name, durationMinutes, performances, id) VALUES 
            ('{trainingReceived.name}',{trainingReceived.durationMinutes}, {trainingReceived.performances}, {trainingReceived.id})"""
    table = "trainings"
    return query, table

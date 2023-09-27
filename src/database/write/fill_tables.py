import pyodbc

from src.api.receiver import WorkoutReceived, TrainingReceived


def add_new_workout(connection: pyodbc.Connection, workoutReceived: WorkoutReceived) -> None:
    cursor = connection.cursor()
    #ToDo: Check if we can avoid the IDENTITY_INSERT setting.
    cursor.execute(f"SET IDENTITY_INSERT workouts ON")
    query = f"""INSERT INTO workouts(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id) VALUES 
            ('{workoutReceived.name}', {workoutReceived.sets}, {workoutReceived.totalRepetitions}, 
            {workoutReceived.maxRepetitions}, {workoutReceived.performances}, {workoutReceived.id})"""
    cursor.execute(query)
    cursor.execute(f"SET IDENTITY_INSERT workouts OFF")
    connection.commit()
    cursor.close()

def add_new_training(connection: pyodbc.Connection, trainingReceived: TrainingReceived) -> None:
    cursor = connection.cursor()
    #ToDo: Check if we can avoid the IDENTITY_INSERT setting.
    cursor.execute(f"SET IDENTITY_INSERT trainings ON")
    query = f"""INSERT INTO trainings(name, durationMinutes, performances, id) VALUES 
            ('{trainingReceived.name}',{trainingReceived.durationMinutes}, {trainingReceived.performances}, {trainingReceived.id})"""
    print(cursor.execute(query))
    cursor.execute(f"SET IDENTITY_INSERT trainings OFF")
    connection.commit()
    cursor.close()

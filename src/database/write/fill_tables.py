import pyodbc

from src.api.receiver import WorkoutReceived


def write_to_workouts_table(connection: pyodbc.Connection, workoutReceived: WorkoutReceived) -> bool:
    cursor = connection.cursor()

    cursor.execute(f"SET IDENTITY_INSERT workouts ON")
    query = f"""INSERT INTO workouts(name, sets, totalRepetitions, maxRepetitionsInSet, performances, id) VALUES 
            ('{workoutReceived.name}', {workoutReceived.sets}, {workoutReceived.totalRepetitions}, 
            {workoutReceived.maxRepetitions}, {workoutReceived.performances}, {workoutReceived.id})"""
    cursor.execute(query)
    cursor.execute(f"SET IDENTITY_INSERT workouts OFF")
    connection.commit()
    cursor.close()

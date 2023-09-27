from typing import Callable, Tuple

import pyodbc
from pydantic import BaseModel

from src.api.receiver import WorkoutReceived


def insert(function: Callable[[BaseModel], Tuple[str, str]], data: BaseModel, connection: pyodbc.Connection) -> None:
    query, table = function(data)
    cursor = connection.cursor()
    # ToDo: Check if we can avoid the IDENTITY_INSERT setting.
    cursor.execute(f"SET IDENTITY_INSERT {table} ON")
    cursor.execute(query)
    cursor.execute(f"SET IDENTITY_INSERT {table} OFF")
    connection.commit()
    cursor.close()


def update_workout(connection: pyodbc, workoutReceived: WorkoutReceived) -> None:
    pass

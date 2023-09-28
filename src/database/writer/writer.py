from typing import Callable, Tuple

import pyodbc
from pydantic import BaseModel


def insert(query_table_provider: Callable[[BaseModel], Tuple[str, str]], data: BaseModel,
           connection: pyodbc.Connection) -> None:
    query, table = query_table_provider(data)
    cursor = connection.cursor()
    # ToDo: Check if we can avoid the IDENTITY_INSERT setting.
    cursor.execute(f"SET IDENTITY_INSERT {table} ON")
    cursor.execute(query)
    cursor.execute(f"SET IDENTITY_INSERT {table} OFF")
    connection.commit()
    cursor.close()


def update(query_table_provider: Callable[[BaseModel], Tuple[str, str]], data: BaseModel,
           connection: pyodbc.Connection) -> None:
    query, table = query_table_provider(data)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

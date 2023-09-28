from typing import Callable, Tuple

import pyodbc
from pydantic import BaseModel


class Writer:
    def __init__(self, connection: pyodbc.Connection) -> None:
        self._connection = connection

    def insert(self, query_table_provider: Callable[[BaseModel], Tuple[str, str]], data: BaseModel) -> None:
        query, table = query_table_provider(data)
        cursor = self._connection.cursor()
        # ToDo: Check if we can avoid the IDENTITY_INSERT setting.
        cursor.execute(f"SET IDENTITY_INSERT {table} ON")
        cursor.execute(query)
        cursor.execute(f"SET IDENTITY_INSERT {table} OFF")
        self._connection.commit()
        cursor.close()

    def update(self, query_table_provider: Callable[[BaseModel], Tuple[str, str]], data: BaseModel,
               connection: pyodbc.Connection) -> None:
        query, table = query_table_provider(data)
        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()
        cursor.close()

import pyodbc

from access.access import get_pyodbc_connection_string


def get_database_connection(password_file: str) -> pyodbc.Connection:
    url = get_pyodbc_connection_string(password_file)
    connection = pyodbc.connect(url)
    return connection

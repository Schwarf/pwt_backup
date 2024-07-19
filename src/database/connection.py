import pyodbc

from database.access.access import get_pyodbc_connection_string


def get_database_connection() -> pyodbc.Connection:
    password_file = "/media/linux_data/projects/misc/database_access/access.txt"
    url = get_pyodbc_connection_string(password_file)
    connection = pyodbc.connect(url)
    try:
        yield connection
    finally:
        connection.close()

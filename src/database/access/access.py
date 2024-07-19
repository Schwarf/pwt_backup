import pyodbc


def get_pyodbc_connection_string(password_file: str) -> str:
    driver = "ODBC Driver 17 for SQL Server"
    server = 'localhost'
    database = 'pwt_backup'
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    print("Username PYODBC", username)
    url = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    return url

def get_sql_alchemy_url(password_file: str) -> str:
    server = 'localhost:1433'
    database = 'pwt_backup'
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    print("Username SQLALCHEMY", username)
    url = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    return url


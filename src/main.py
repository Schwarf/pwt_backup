import argparse
import sys
from sqlalchemy import create_engine
from database.access.access import get_database_connection, get_sql_alchemy_url
from database.scheme.conventions import SchemeDefinition
from database.scheme.pwt_tables import *
def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()

    connection = get_database_connection(arguments.password_file)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sys.databases")
    for row in cursor.fetchall():
         print(row)
    connection.close()

    #SchemeDefinition.metadata.create_all(engine)
if __name__ == "__main__":
    main()

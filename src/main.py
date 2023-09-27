import argparse
import sys
from sqlalchemy import create_engine

from conventions import Base
from database.access.access import get_database_connection, get_sql_alchemy_url

def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()
    engine = create_engine(get_sql_alchemy_url(arguments.password_file))
    connection = get_database_connection(arguments.password_file)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sys.databases")
    cursor.execute('''
    		CREATE TABLE products (
    			product_id int,
    			product_name nvarchar(50),
    			price int
    			)
                   ''')

    connection.commit()

#    SchemeDefinition.metadata.create_all(engine)
if __name__ == "__main__":
    main()

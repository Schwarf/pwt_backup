import argparse
import sys
from sqlalchemy import create_engine

from conventions import Base
from database.connection import get_database_connection
from src.api.receiver import WorkoutReceived, TrainingReceived
from write.fill_tables import add_new_workout, add_new_training


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()
    connection = get_database_connection(arguments.password_file)
    training = TrainingReceived(name="Jogging", durationMinutes=50, performances=1, id=1)
    #workout = WorkoutReceived(name="Hallo", sets=3, totalRepetitions=22, maxRepetitions=10, performances=0, id=1)
    #add_new_workout(connection, workout)
    add_new_training(connection, training)

    # cursor = connection.cursor()
    # cursor.execute("SELECT name FROM sys.databases")
    # cursor.execute('''
    # 		CREATE TABLE products (
    # 			product_id int,
    # 			product_name nvarchar(50),
    # 			price int
    # 			)
    #                ''')
    #
    # connection.commit()

#    SchemeDefinition.metadata.create_all(engine)
if __name__ == "__main__":
    main()

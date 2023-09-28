import argparse
import sys
from sqlalchemy import create_engine

from conventions import Base
from database.connection import get_database_connection
from src.api.received_objects import WorkoutReceived, TrainingReceived
from writer.writer import Writer
from writer.queries import *


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()
    database_writer = Writer(get_database_connection(arguments.password_file))
    training = TrainingReceived(name="Jogging", durationMinutes=50, performances=1, id=1)
    workout = WorkoutReceived(name="Hallo", sets=3, totalRepetitions=22, maxRepetitions=10, performances=0, id=1)
    database_writer.insert(workout_query, workout)
    database_writer.insert(training_query, training)
    #training_update = TrainingReceived(name="Jogging", durationMinutes=50, performances=20, id=2)
    #workout_update = WorkoutReceived(name="Hallo", sets=3, totalRepetitions=22, maxRepetitions=10, performances=3, id=2)
    #update(update_training_query, training_update, connection)
    #update(update_workout_query, workout_update, connection)
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

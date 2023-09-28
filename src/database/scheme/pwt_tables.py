from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship
from src.database.scheme.conventions import Base, InsertionDateTime


class Workout(Base, InsertionDateTime):
    __tablename__ = "workouts"
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    totalRepetitions = Column(Integer, nullable=False)
    maxRepetitionsInSet = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True)

class Training(Base, InsertionDateTime):
    __tablename__ = "trainings"
    name = Column(String, nullable=False)
    durationMinutes = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True)


class WorkoutTimestamp(Base, InsertionDateTime):
    __tablename__ = "workout_timestamps"
    id = Column(Integer, nullable=False, primary_key=True)
    workoutId = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    workout = relationship("Workout")

class TrainingTimestamp(Base, InsertionDateTime):
    __tablename__ = "training_timestamps"
    id = Column(Integer, nullable=False, primary_key=True)
    trainingId = Column(Integer, ForeignKey("trainings.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    training = relationship("Training")

class Synchronization(Base,InsertionDateTime):
    __tablename__ = "synchronization_dates"
    id = Column(Integer, nullable=False, primary_key=True)
    date = Column(DateTime, nullable=False)

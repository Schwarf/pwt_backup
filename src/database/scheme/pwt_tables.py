from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship
from conventions import SchemeDefinition


class Workout(SchemeDefinition):
    __tablename__ = "workouts"
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    totalRepetitions = Column(Integer, nullable=False)
    maxRepetitionsInSet = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False)

class Training(SchemeDefinition):
    __tablename__ = "trainings"
    name = Column(String, nullable=False)
    durationMinutes = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False)


class WorkoutTimestamp(SchemeDefinition):
    __tablename__ = "workout_timestamps"
    id = Column(Integer, nullable=False)
    workoutId = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    workout = relationship("Workout")

class TrainingTimestamp(SchemeDefinition):
    __tablename__ = "training_timestamps"
    id = Column(Integer, nullable=False)
    workoutId = Column(Integer, ForeignKey("trainings.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    training = relationship("Training")
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Workout(Base):
    __tablename__ = "workouts"
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    totalRepetitions = Column(Integer, nullable=False)
    maxRepetitionsInSet = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False)

class Training(Base):
    __tablename__ = "trainings"
    name = Column(String, nullable=False)
    durationMinutes = Column(Integer, nullable=False)
    performances = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False)


class WorkoutTimestamp(Base):
    __tablename__ = "workout_timestamps"
    id = Column(Integer, nullable=False)
    workoutId = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    workout = relationship("Workout")

class TrainingTimestamp(Base):
    __tablename__ = "training_timestamps"
    id = Column(Integer, nullable=False)
    workoutId = Column(Integer, ForeignKey("trainings.id", ondelete="CASCADE"))
    timestamp = Column(BigInteger, nullable=False)
    # Define a relationship to the Workout model (assuming the name of the related table is "workout")
    training = relationship("Training")
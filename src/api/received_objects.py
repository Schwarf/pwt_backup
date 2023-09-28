from pydantic import BaseModel


class WorkoutReceived(BaseModel):
    name: str
    sets: int
    totalRepetitions: int
    maxRepetitions: int
    performances: int
    id: int


class TrainingReceived(BaseModel):
    name: str
    durationMinutes: int
    performances: int
    id: int


class WorkoutTimestampReceived(BaseModel):
    id: int
    workoutId: int
    timestamp: int


class TrainingTimestampReceived(BaseModel):
    id: int
    trainingId: int
    timestamp: int

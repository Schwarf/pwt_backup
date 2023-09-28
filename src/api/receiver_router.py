from fastapi import FastAPI


app = FastAPI()


@app.post("/workouts/")
async def push_workout(workout: WorkoutReceived):


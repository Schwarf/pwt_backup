from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
# NOTE: There is functionality for path parameters containing paths.

app = FastAPI()

@app.get("/models")
async def get_models():
    response = {"Choose a model by name:" : "alexnet, lenet, resnet",
                "Model 1" : "resnet",
                "Model 2" : "alexnet",
                "Model 3" : "lenet"}
    return response

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
from typing import Union
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return {"sucker": "Sepp"}


@app.get("/items/{item_id}")
def read_item(item_id: float):
    return {"item_id": item_id}

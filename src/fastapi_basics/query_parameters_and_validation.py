from typing import Union, List

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[Union[str, None], Query(min_length=3, max_length=50)] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# http://127.0.0.1:8000/items2/?q=ein&q=zwei&q=dero
@app.get("/items2/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    result = {}
    for i, item in enumerate(q):
        result[f"{i}"] = item
    return result
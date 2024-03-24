from typing import Union
from random import randint

from fastapi import FastAPI

from models import Item
from utils.utils import file_opener

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/phrase")
def get_phrase():
    # TODO: Change for Database info
    phrases = file_opener("Filosofía.md")
    phrase_id = randint(0, len(phrases) - 1)
    return {
        "id": phrase_id,
        "phrase": phrases[phrase_id][0],
        "author": phrases[phrase_id][1]
        }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

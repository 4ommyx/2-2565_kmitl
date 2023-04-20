from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Name(BaseModel):

    name: str
    age: int

nameDb = [
    {
    "name" : "nattawut",
    "Age" : 19
    },
    {
    "name" : "Music",
    "Age" : 18
    },
    {
    "name" : "Kanjama",
    "Age" : 40
    }
]

app = FastAPI()

@app.get('/showData')
async def root():
    return nameDb

@app.get('/passID/{id}')
async def passInt(id:int):
    name = nameDb[id-1]
    return name

@app.post('/paasData')
async def passData(name:Name):
    nameDb.append(name)
    print(nameDb)
    return nameDb[-1]

@app.delete('/deleteID/{id}')
async def deleteData(id:int):
    nameDe = nameDb[id-1]
    nameDb.pop(id-1)
    return f" {nameDe['name']} deleted !"
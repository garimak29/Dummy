from typing import Optional
from datetime import datetime
from fastapi import FastAPI

from pydantic import BaseModel
app = FastAPI()

class Train(BaseModel):
    id: int
    name: str
    ExpectedArrTime: datetime = None
    ExpectedDepartureTime: datetime = None


class DailyData(BaseModel):
    TrainId: int
    ActualArrTime: datetime = None
    ActualDepartureTime: datetime = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/train/{id}")
def read_train(id: int, q: Optional[str] = None):
    return {"train_id": id, "q": q}


@app.post("/train/new")
def create_train(train: Train):
    return train

@app.put("/train/update/{id}")
def update_train(id : int , train: Train):
    return train

@app.post("/Daily/create")
def create_Daily(daily: DailyData):
    return daily

@app.put("/Daily/update/{train_id}")
def update_Daily(train_id : int , daily: DailyData):
    return daily
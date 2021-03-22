from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class DailyDataBase(BaseModel):
    actualArvTime: datetime=None
    actualDepartureTime: datetime=None

class DailyDataCreate(BaseModel):
    pass


class DailyData(DailyDataBase):
    id: int
    trainId: int

    class Config:
        orm_mode = True


class TrainBase(BaseModel):
    name: str



class TrainCreate(TrainBase):
    expectedArvTime: datetime
    expectedDepartureTime: datetime


class Train(TrainBase):
    id: int
    dailyData: List[DailyData] = []

    class Config:
        orm_mode = True

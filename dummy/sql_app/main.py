from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/trains/", response_model=schemas.Train)
def create_train(train: schemas.TrainCreate, db: Session = Depends(get_db)):
    db_train = crud.get_train_by_name(db, name=train.name)
    if db_train:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_train(db=db, train=train)



@app.get("/trains/", response_model=List[schemas.Train])
def read_trains(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trains = crud.get_trains(db, skip=skip, limit=limit)
    return trains

@app.put("/trains/{train_id}/", response_model=schemas.Train)
def update_train(train_id: int, train : schemas.TrainUpdate , db: Session = Depends(get_db)):
    db_train = crud.get_train(db, train_id=train_id)
    if db_train is None:
        raise HTTPException(status_code=404, detail="Train not found")
    return crud.update_train_by_id(db=db, train=train , train_id=train_id)



@app.get("/trains/{train_id}", response_model=schemas.Train)
def read_train(train_id: int, db: Session = Depends(get_db)):
    db_train = crud.get_train(db, train_id=train_id)
    if db_train is None:
        raise HTTPException(status_code=404, detail="Train not found")
    return db_train

@app.post("/trains/{trainId}/dailyData/", response_model=schemas.DailyData)
def create_dailyData_for_train(
    trainId: int, dailyData: schemas.DailyDataCreate, db: Session = Depends(get_db)
):
    return crud.create_train_dailyData(db=db, dailyData=dailyData, trainId=trainId)


@app.put("/trains/{trainId}/dailyData/update/", response_model=schemas.DailyData)
def update_dailyData_for_train(
    trainId: int, dailyData: schemas.DailyDataCreate, db: Session = Depends(get_db)
):
    return crud.update_train_dailyData(db=db, dailyData=dailyData, trainId=trainId)


@app.get("/dailyData/", response_model=List[schemas.DailyData])
def read_dailyData(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dailyData = crud.get_dailyData(db, skip=skip, limit=limit)
    return dailyData
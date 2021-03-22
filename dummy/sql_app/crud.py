from sqlalchemy import DateTime
from sqlalchemy.orm import Session
from . import models, schemas

def get_train(db: Session, train_id: int):

    return db.query(models.Train).filter(models.Train.id == train_id).first()




def get_train_by_name(db: Session, name: str):

    return db.query(models.Train).filter(models.Train.name == name).first()


def get_trains(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Train).offset(skip).limit(limit).all()



def create_train(db: Session, train: schemas.TrainCreate):
    db_train = models.Train(name=train.name, expectedArvTime=train.expectedArvTime , expectedDepartureTime= train.expectedDepartureTime )
    db.add(db_train)
    db.commit()
    db.refresh(db_train)
    return db_train



def get_dailyData(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.DailyData).offset(skip).limit(limit).all()



def create_train_dailyData(db: Session, dailyData: schemas.DailyDataBase, trainId: int):
    db_dailyData = models.DailyData(**dailyData.dict(), trainId=trainId )
    db.add(db_dailyData)
    db.commit()
    db.refresh(db_dailyData)
    return db_dailyData

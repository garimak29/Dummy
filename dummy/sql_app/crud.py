from sqlalchemy import DateTime
from sqlalchemy.orm import Session
from . import models, schemas

def get_train(db: Session, train_id: int):

    return db.query(models.Train).filter(models.Train.id == train_id).first()




def get_train_by_name(db: Session, train: schemas.TrainCreate , name: str):

    return db.query(models.Train).filter(models.Train.name == name).first()


def update_train_by_id(db: Session, train: schemas.TrainUpdate, train_id: int):
    db_train=db.query(models.Train).filter(models.Train.id == train_id).first();
    db_train.name = train.name
    db_train.expectedArvTime = train.expectedArvTime
    db_train.expectedDepartureTime = train.expectedDepartureTime
    db.add(db_train)
    db.commit()
    db.refresh(db_train)
    return db_train



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



def create_train_dailyData(db: Session, dailyData: schemas.DailyDataCreate, trainId: int):
    db_dailyData = models.DailyData(trainId=trainId , actualArvTime=dailyData.actualArvTime , actualDepartureTime= dailyData.actualDepartureTime )
    db.add(db_dailyData)
    db.commit()
    db.refresh(db_dailyData)
    return db_dailyData


def update_train_dailyData(db: Session, dailyData: schemas.DailyDataCreate, trainId: int):
   # db_dailyData = models.DailyData(actualArvTime=dailyData.actualArvTime , actualDepartureTime= dailyData.actualDepartureTime )
    db_dailyData = db.query(models.DailyData).filter(models.DailyData.trainId == trainId).first()
    db_dailyData.actualArvTime = dailyData.actualArvTime
    db_dailyData.actualDepartureTime = dailyData.actualDepartureTime
    db.add(db_dailyData)
    db.commit()
    db.refresh(db_dailyData)
    return db_dailyData



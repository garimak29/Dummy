from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Train(Base):
    __tablename__ = "trains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    expectedArvTime = Column(DateTime)
    expectedDepartureTime = Column(DateTime)
    actualData = relationship("DailyData" , back_populates="train")



class DailyData(Base):
    __tablename__ = "dailyData"

    id = Column(Integer, primary_key=True, index=True)
    trainId = Column(Integer, ForeignKey("trains.id"))
    actualArvTime = Column(DateTime)
    actualDepartureTime = Column(DateTime)

    train = relationship("Train", back_populates="actualData")


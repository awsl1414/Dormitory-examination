from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db.database import Base


class Sanitation(Base):
    __tablename__ = 'SanitationTable'

    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    WeekNumber = Column(Integer)
    Weekday = Column(Integer)
    Status = Column(String)
    DormID = Column(Integer, ForeignKey('DormTable.DormID'))

    dorm = relationship('Dorm', back_populates='sanitations')

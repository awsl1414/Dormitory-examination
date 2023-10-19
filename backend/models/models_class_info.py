from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, relationship

from db.database import Base


class Grade(Base):
    __tablename__ = 'GradeTable'

    GradeID = Column(Integer, primary_key=True, autoincrement=True)
    GradeName = Column(String, nullable=False)


class Major(Base):
    __tablename__ = 'MajorTable'

    MajorID = Column(Integer, primary_key=True, autoincrement=True)
    MajorName = Column(String, nullable=False)
    GradeID = Column(Integer, ForeignKey('GradeTable.GradeID'))

    grade = relationship('Grade', back_populates='majors')


class Classes(Base):
    __tablename__ = 'ClassTable'

    ClassID = Column(Integer, primary_key=True, autoincrement=True)
    ClassName = Column(String, nullable=False)
    MajorID = Column(Integer, ForeignKey('MajorTable.MajorID'))

    major = relationship('Major', back_populates='classes')


class Dorm(Base):
    __tablename__ = 'DormTable'

    DormID = Column(Integer, primary_key=True, autoincrement=True)
    DormName = Column(String, nullable=False)
    ClassID = Column(Integer, ForeignKey('ClassTable.ClassID'))

    sanitations = relationship("Sanitation", back_populates="dorm")
    class_ = relationship('Classes', back_populates='dorms')


Grade.majors = relationship('Major', order_by=Major.MajorID, back_populates='grade')
Major.classes = relationship('Classes', order_by=Classes.ClassID, back_populates='major')
Classes.dorms = relationship('Dorm', order_by=Dorm.DormID, back_populates='class_')

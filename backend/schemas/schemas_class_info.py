from pydantic import BaseModel
from typing import List


class CollegeCreate(BaseModel):
    CollegeName: str


class GradeCreate(BaseModel):
    GradeName: str


class MajorCreate(BaseModel):
    MajorName: str


class ClassCreate(BaseModel):
    ClassName: str


class DormCreate(BaseModel):
    DormName: str


class ClassInfoIn(BaseModel):
    info: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "info": ["双能 20 自动化 01 123", "双能 21 机器人 02 456", "软院 22 数媒体 03 789"]
            }
        }


class SanitationCreate(BaseModel):
    WeekNumber: int
    Weekday: int
    Status: str
    DormID: int

    class Config:
        json_schema_extra = {
            "example1": {"WeekNumber": 1, "Weekday": 2, "Status": "优秀", "DormID": 1},
            "example2": {"WeekNumber": 2, "Weekday": 3, "Status": "优秀", "DormID": 2},
        }

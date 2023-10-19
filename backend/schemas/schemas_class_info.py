from pydantic import BaseModel
from typing import List


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
                "info": [
                    "20 自动化 01 123",
                    "21 机器人 02 224"
                ]
            }
        }


class SanitationCreate(BaseModel):
    WeekNumber: int
    Weekday: int
    Status: str
    DormID: int

    class Config:
        json_schema_extra = {
            "example":
                {
                    "WeekNumber": 1,
                    "Weekday": 1,
                    "Status": "优秀",
                    "DormID": 1
                }
        }

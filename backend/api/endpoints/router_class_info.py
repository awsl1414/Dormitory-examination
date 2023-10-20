# 在api/endpoints/router_class_info.py中添加或修改以下代码

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas_class_info import (
    GradeCreate,
    MajorCreate,
    ClassCreate,
    DormCreate,
    ClassInfoIn,
    SanitationCreate,
)
from db.database import get_db
from crud.crud_class_info import (
    query_info,
    create_grade,
    create_major,
    create_class,
    create_dorm,
    create_sanitation,
)

router_class_info = APIRouter()


@router_class_info.get("/query_info")
def query_info_api(
    grade: Optional[str] = None,
    college: Optional[str] = None,
    major: Optional[str] = None,
    classes: Optional[str] = None,
    dorm: Optional[str] = None,
    weeknum: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    query_ = query_info(db, college, grade, major, classes, dorm, weeknum, status)
    return query_


@router_class_info.post("/create_info")
def create_info_api(input_data: ClassInfoIn, db: Session = Depends(get_db)):
    results = []
    for info in input_data.info:
        grade_name, major_name, class_name, dorm_name = info.split()

        grade = create_grade(db, grade_name=grade_name)
        major = create_major(db, major_name=major_name, grade_id=grade.GradeID)
        class_ = create_class(db, class_name=class_name, major_id=major.MajorID)
        dorm = create_dorm(db, dorm_name=dorm_name, class_id=class_.ClassID)

        results.append(
            {
                "grade": grade.GradeName,
                "major": major.MajorName,
                "class": class_.ClassName,
                "dorm": dorm.DormName,
            }
        )

    return results


@router_class_info.post("/create_sanitation", response_model=SanitationCreate)
def create_sanitation_api(sanitation: SanitationCreate, db: Session = Depends(get_db)):
    return create_sanitation(db, sanitation_data=sanitation)

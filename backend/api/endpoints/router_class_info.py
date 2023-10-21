# 在api/endpoints/router_class_info.py中添加或修改以下代码

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas_class_info import (
    CollegeCreate,
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
    create_college,
    create_grade,
    create_major,
    create_class,
    create_dorm,
    create_sanitation,
)

router_class_info = APIRouter()


# TODO 综合查询
@router_class_info.get("/query_info")
def query_info_api(
    college: Optional[str] = None,
    grade: Optional[str] = None,
    major: Optional[str] = None,
    classes: Optional[str] = None,
    dorm: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    result = query_info(db, college, grade, major, classes, dorm)
    return result


@router_class_info.post("/create_info")
def create_info_api(input_data: ClassInfoIn, db: Session = Depends(get_db)):
    results = []
    for info in input_data.info:
        college_name, grade_name, major_name, class_name, dorm_name = info.split()
        # print(college_name, grade_name, major_name, class_name, dorm_name)

        college = create_college(db, college_name=college_name)
        grade = create_grade(db, grade_name=grade_name, college_id=college.CollegeID)
        major = create_major(db, major_name=major_name, grade_id=grade.GradeID)
        class_ = create_class(db, class_name=class_name, major_id=major.MajorID)
        dorm = create_dorm(db, dorm_name=dorm_name, class_id=class_.ClassID)

        results.append(
            {
                "college": college.CollegeName,
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

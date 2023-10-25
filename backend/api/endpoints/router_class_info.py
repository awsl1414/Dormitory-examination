# 在api/endpoints/router_class_info.py中添加或修改以下代码

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models_class_info import College, Grade, Major, Classes, Dorm
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
    query_info_all,
    create_college,
    create_grade,
    create_major,
    create_class,
    create_dorm,
    create_sanitation,
)

router_class_info = APIRouter()


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
    result = query_info(db, college, grade, major, classes, dorm, skip, limit)
    return result


@router_class_info.get("/query_test")
def query_test(name: str, db: Session = Depends(get_db)):
    result = db.query(College).filter(College.CollegeName == name).first()
    print(result.CollegeID)


# TODO 总查询
@router_class_info.get("/query_info_all")
def query_info_all_api(db: Session = Depends(get_db)):
    query_info_all(db)


@router_class_info.post("/create_info")
def create_info_api(input_data: ClassInfoIn, db: Session = Depends(get_db)):
    temp = {}
    results = []
    is_none = []

    for info in input_data.info:
        college_name, grade_name, major_name, class_name, dorm_name = info.split()
        # print(college_name, grade_name, major_name, class_name, dorm_name)
        if not db.query(College).filter(College.CollegeName == college_name).first():
            college = create_college(db, college_name=college_name)
            temp.update({"college": college.CollegeName})
        else:
            is_none.append(f"{college_name}已存在")
            # TODO
            college_id = (
                db.query(College)
                .filter(College.CollegeName == college_name)
                .first()
                .CollegeID
            )
        if not db.query(Grade).filter(Grade.GradeName == grade_name).first():
            grade = create_grade(db, grade_name=grade_name, college_id=college_id)
            temp.update({"grade": grade.GradeName})
        else:
            is_none.append(f"{grade_name}已存在")
            grade_id = (
                db.query(Grade).filter(Grade.GradeName == grade_name).first().GradeID
            )
        if not db.query(Major).filter(Major.MajorName == major_name).first():
            major = create_major(db, major_name=major_name, grade_id=grade_id)
            temp.update({"major": major.MajorName})
        else:
            is_none.append(f"{major_name}已存在")
            major_id = (
                db.query(Major).filter(Major.MajorName == major_name).first().MajorID
            )
        if not db.query(Classes).filter(Classes.ClassName == class_name).first():
            class_ = create_class(db, class_name=class_name, major_id=major_id)
            temp.update({"class": class_.ClassName})
        else:
            is_none.append(f"{class_name}已存在")
            class_id = (
                db.query(Classes)
                .filter(Classes.ClassName == class_name)
                .first()
                .ClassID
            )
        if not db.query(Dorm).filter(Dorm.DormName == dorm_name).first():
            dorm = create_dorm(db, dorm_name=dorm_name, class_id=class_id)
            temp.update({"dorm": dorm.DormName})
        else:
            is_none.append(f"{dorm_name}已存在")

        results.append(temp)

    #     print("内", temp)
    # print("外", temp)
    # print(results)
    return is_none, results


@router_class_info.post("/create_sanitation", response_model=SanitationCreate)
def create_sanitation_api(sanitation: SanitationCreate, db: Session = Depends(get_db)):
    return create_sanitation(db, sanitation_data=sanitation)

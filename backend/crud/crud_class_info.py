from typing import Optional
from sqlalchemy.orm import Session
from models.models_class_info import College, Grade, Major, Classes, Dorm
from models.models_sanitation import Sanitation
from schemas.schemas_class_info import SanitationCreate


# TODO 综合查询
def query_info(
    db: Session,
    college: Optional[str] = None,
    grade: Optional[str] = None,
    major: Optional[str] = None,
    classes: Optional[str] = None,
    dorm: Optional[str] = None,
    weeknum: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
):
    if grade:
        result = db.query

    # grade = (
    #     db.query(Sanitation)
    #     .filter(Sanitation.Status == f"{status}")
    #     .offset(skip)
    #     .limit(limit)
    #     .all()
    # )

    # return grade


def create_college(db: Session, college_name: str) -> College:
    college = College(CollegeName=college_name)
    db.add(college)
    db.commit()
    db.refresh(college)
    return college


def create_grade(db: Session, grade_name: str) -> Grade:
    grade = Grade(GradeName=grade_name)
    db.add(grade)
    db.commit()
    db.refresh(grade)
    return grade


def create_major(db: Session, major_name: str, grade_id: int) -> Major:
    major = Major(MajorName=major_name, GradeID=grade_id)
    db.add(major)
    db.commit()
    db.refresh(major)
    return major


def create_class(db: Session, class_name: str, major_id: int) -> Classes:
    class_ = Classes(ClassName=class_name, MajorID=major_id)
    db.add(class_)
    db.commit()
    db.refresh(class_)
    return class_


def create_dorm(db: Session, dorm_name: str, class_id: int) -> Dorm:
    dorm = Dorm(DormName=dorm_name, ClassID=class_id)
    db.add(dorm)
    db.commit()
    db.refresh(dorm)
    return dorm


def create_sanitation(db: Session, sanitation_data: SanitationCreate) -> Sanitation:
    sanitation = Sanitation(**sanitation_data.model_dump())
    db.add(sanitation)
    db.commit()
    db.refresh(sanitation)
    return sanitation

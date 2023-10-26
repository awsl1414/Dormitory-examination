from typing import Optional
from sqlalchemy.orm import Session
from models.models_class_info import College, Grade, Major, Classes, Dorm
from models.models_sanitation import Sanitation
from schemas.schemas_class_info import SanitationCreate
from utils import Response200, Response400


def query_info(
    db: Session,
    college: Optional[str] = None,
    college_to_grade: Optional[str] = None,
    grade_to_major: Optional[str] = None,
    major_to_classes: Optional[str] = None,
    classes_to_dorm: Optional[str] = None,
    dorm_to_sanitation: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
):
    if college:
        result = db.query(College).offset(skip).limit(limit).all()
        return result

    if college_to_grade:
        result = (
            db.query(Grade)
            .join(College)
            .filter(College.CollegeName == college_to_grade)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result
    if grade_to_major:
        result = (
            db.query(Major)
            .join(Grade)
            .filter(Grade.GradeName == grade_to_major)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result
    if major_to_classes:
        result = (
            db.query(Classes)
            .join(Major)
            .filter(Major.MajorName == major_to_classes)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result
    if classes_to_dorm:
        result = (
            db.query(Dorm)
            .join(Classes)
            .filter(Classes.ClassName == classes_to_dorm)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result
    if dorm_to_sanitation:
        result = (
            db.query(Sanitation)
            .join(Dorm)
            .filter(Dorm.DormName == dorm_to_sanitation)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result

    return "No data"


def create_college(db: Session, college_name: str) -> College:
    if not db.query(College).filter(College.CollegeName == college_name).first():
        # temp.update({"college": college.CollegeName})
        college = College(CollegeName=college_name)
        db.add(college)
        db.commit()
        db.refresh(college)
        return college
    return Response400()


def create_grade(db: Session, grade_name: str, college_id: int) -> Grade:
    if not db.query(Grade).filter(Grade.GradeName == grade_name).first():
        grade = Grade(GradeName=grade_name, CollegeID=college_id)
        db.add(grade)
        db.commit()
        db.refresh(grade)
        return grade
    return Response400()


def create_major(db: Session, major_name: str, grade_id: int) -> Major:
    if not db.query(Major).filter(Major.MajorName == major_name).first():
        major = Major(MajorName=major_name, GradeID=grade_id)
        db.add(major)
        db.commit()
        db.refresh(major)
        return major
    return Response400()


def create_class(db: Session, class_name: str, major_id: int) -> Classes:
    if not db.query(Classes).filter(Classes.ClassName == class_name).first():
        class_ = Classes(ClassName=class_name, MajorID=major_id)
        db.add(class_)
        db.commit()
        db.refresh(class_)
        return class_
    return Response400()


def create_dorm(db: Session, dorm_name: str, class_id: int) -> Dorm:
    if not db.query(Dorm).filter(Dorm.DormName == dorm_name).first():
        dorm = Dorm(DormName=dorm_name, ClassID=class_id)
        db.add(dorm)
        db.commit()
        db.refresh(dorm)
        return dorm
    return Response400()


def create_sanitation(db: Session, sanitation_data: SanitationCreate) -> Sanitation:
    sanitation = Sanitation(**sanitation_data.model_dump())
    db.add(sanitation)
    db.commit()
    db.refresh(sanitation)
    return sanitation


def update_college(db: Session, college_name: str, re_college_name: str) -> College:
    if result := db.query(College).filter(College.CollegeName == college_name).first():
        college = result.CollegeName = re_college_name
        db.commit()
        return Response200(data=college)
    return Response400()


def update_grade(db: Session, grade_name: str, re_grade_name: str) -> Grade:
    if result := db.query(Grade).filter(Grade.GradeName == grade_name).first():
        grade = result.GradeName = re_grade_name
        db.commit()
        return Response200(data=grade)
    return Response400()


def update_major(db: Session, major_name: str, re_major_name: str) -> Major:
    if result := db.query(Major).filter(Major.MajorName == major_name).first():
        major = result.MajorName = re_major_name
        db.commit()
        return Response200(data=major)
    return Response400()


def update_classes(db: Session, classes_name: str, re_classes_name: str) -> Classes:
    if result := db.query(Classes).filter(Classes.ClassName == classes_name).first():
        classes = result.ClassName = re_classes_name
        db.commit()
        return Response200(data=classes)
    return Response400()


def update_dorm(db: Session, dorm_name: str, re_dorm_name: str) -> Dorm:
    if result := db.query(Dorm).filter(Dorm.DormName == dorm_name).first():
        dorm = result.DormName = re_dorm_name
        db.commit()
        return Response200(data=dorm)
    return Response400()

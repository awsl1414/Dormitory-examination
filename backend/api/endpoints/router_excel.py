from fastapi import FastAPI, Response, Depends, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from db.database import get_db  # 确保这是您的SQLAlchemy数据库连接的正确导入路径
from utils import generate_excel

router_excel = APIRouter()


@router_excel.get("/download_excel/")
def download_excel(db: Session = Depends(get_db)):
    excel_data = generate_excel(db)
    response = StreamingResponse(iter([excel_data.getvalue()]),
                                 media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response.headers["Content-Disposition"] = "attachment; filename=sanitation_records.xlsx"
    return response

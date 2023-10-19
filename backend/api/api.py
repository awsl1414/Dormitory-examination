from fastapi import APIRouter

from api.endpoints import router_user, router_login, router_class_info, router_excel

api_router = APIRouter()
api_router.include_router(router_user.router_user, prefix="/user", tags=["用户"])
api_router.include_router(router_login.router_login, prefix="/login", tags=["登录"])
api_router.include_router(router_class_info.router_class_info, prefix="/class_info", tags=["基本信息"])
api_router.include_router(router_excel.router_excel, prefix="/excel", tags=["导入导出"])

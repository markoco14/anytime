""" Admin routes """
from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.auth import auth_service
from app.core.database import get_db

from app.repositories import user_repository as UserRepository

router = APIRouter(
    prefix="/admin",
    tags=["admin"],

)
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def read_admin_home_page(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
):
    """Returns admin section home page"""
    if not auth_service.get_session_cookie(request.cookies):
        return templates.TemplateResponse(
            request=request,
            name="website/web-home.html",
            headers={"HX-Redirect": "/"},
        )

    current_user = auth_service.get_current_session_user(
        db=db, cookies=request.cookies)

    if not current_user.is_admin:
        return templates.TemplateResponse(
            request=request,
            name="website/web-home.html",
            headers={"HX-Redirect": "/"},
        )
    
    user_page_data = {
        "display_name": current_user.display_name.split(" ")[0],
        "is_admin": current_user.is_admin
    }

    context = {
        "user_data": user_page_data,
        "request": request,
    }

    return templates.TemplateResponse(
        request=request,
        name="admin/admin-home.html",
        context=context
    )



@router.get("/users", response_class=HTMLResponse)
def list_users(
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    ):
    """List users"""
    if not auth_service.get_session_cookie(request.cookies):
        return templates.TemplateResponse(
            request=request,
            name="website/web-home.html",
            headers={"HX-Redirect": "/"},
        )
    
    current_user = auth_service.get_current_session_user(db=db, cookies=request.cookies)

    if not current_user.is_admin:
        return templates.TemplateResponse(
            request=request,
            name="website/web-home.html",
            headers={"HX-Redirect": "/"},
        )

    
    users = UserRepository.list_users(db=db)
    headings = ["Display name", "Actions"]

    user_page_data = {
        "display_name": current_user.display_name.split(" ")[0],
        "is_admin": current_user.is_admin
    }
    
    context = {
        "user_data": user_page_data,
        "request": request,
        "users": users,
        "headings": headings
    }
    
    return templates.TemplateResponse(
        request=request,
        name="admin/users.html",
        context=context
    )

# @router.get("/sessions", response_class=HTMLResponse)
# def list_sessions(
#     request: Request,
#     db: Annotated[Session, Depends(get_db)]
#     ):
#     """List sessions"""
#     if not auth_service.get_session_cookie(request.cookies):
#         return templates.TemplateResponse(
#             request=request,
#             name="website/web-home.html",
#             headers={"HX-Redirect": "/"},
#         )
    
#     current_user = auth_service.get_current_session_user(
#         db=db, cookies=request.cookies)

#     if not current_user.is_admin:
#         return templates.TemplateResponse(
#             request=request,
#             name="website/web-home.html",
#             headers={"HX-Redirect": "/"},
#         )
    
#     sessions = session_repository.list_sessions(db=db)
#     headings = ["ID", "Session Token", "User ID", "Expiry date", "Actions"]
#     context = {
#         "request": request,
#     "sessions": sessions,
#     "headings": headings
#     }
#     return templates.TemplateResponse(
#         request=request,
#         name="admin/sessions.html",
#         context=context
#     )
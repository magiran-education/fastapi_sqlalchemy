from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.manager import get_user_manager
from auth.database import AuthUser


auth_router = APIRouter()


fastapi_users = FastAPIUsers[AuthUser, int](get_user_manager, [auth_backend])
current_user = fastapi_users.current_user()


auth_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))


@auth_router.get("/protected-route")
def protected_route(user: AuthUser = Depends(current_user)):
    return f"Hello, {user.username}"


@auth_router.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

from fastapi import FastAPI
from apps.first_app.router import first_app_router
# from apps.auth.router import auth_router


app = FastAPI(title="Trading App")

app.include_router(first_app_router, prefix="/first_app", tags=["first_app"])
# app.include_router(auth_router, prefix="/auth", tags=["auth"])  # выкл из-за LOGIN_BAD_CREDENTIALS во время логина

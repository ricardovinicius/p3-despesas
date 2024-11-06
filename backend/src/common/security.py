from datetime import timedelta
from typing import Annotated
from fastapi import Depends
from fastapi_jwt import JwtAccessBearerCookie, JwtRefreshBearer

from src.common.settings import get_settings


class SecurityConfig():
    settings = get_settings()

    access_security = JwtAccessBearerCookie(
        secret_key=settings.jwt_secret_key,
        auto_error=False,
        access_expires_delta=timedelta(hours=12) 
    )

    refresh_security = JwtRefreshBearer(
        secret_key=settings.jwt_secret_key, 
        auto_error=True  
    )

SecurityDep = Annotated[SecurityConfig, Depends(SecurityConfig)]
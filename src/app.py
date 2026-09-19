from fastapi import FastAPI

from api import racine, login_service, logout_service, signup_service, user_service

_title = "Alpha 1"

_description = "This is alpha 1 openAPI manifest."

_version = "0.0.2"

app = FastAPI(
    title=_title,
    description=_description,
    version=_version
)
app.include_router(racine)
app.include_router(login_service)
app.include_router(logout_service)
app.include_router(signup_service)
app.include_router(user_service)
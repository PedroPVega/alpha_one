from fastapi import APIRouter, HTTPException, Response

from models import LogInRequest, AuthResponse

from core import handle_login_request

log_in_router = APIRouter()

@log_in_router.post("/login", response_model= AuthResponse)
def log_in(payload: LogInRequest, response: Response):
    result: tuple[AuthResponse, str] | None = handle_login_request(payload)
    if not result:
        raise HTTPException(status_code=401,
                            detail= "Incorrect email or password")

    response.set_cookie(key="token", value=result[1])
    return result[0]
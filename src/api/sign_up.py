from fastapi import APIRouter, HTTPException, Response

from models import SignUpRequest, AuthResponse

from core import handle_signup_request

sign_up_router = APIRouter()

@sign_up_router.post("/signup", response_model= AuthResponse)
def sign_in(payload: SignUpRequest, response: Response):
    result: tuple[AuthResponse, str] | None = handle_signup_request(payload)
    if not result:
        raise HTTPException(status_code=500,
                            detail="failed to create user")
    
    response.set_cookie(key="token", value=result[1])
    return result[0]
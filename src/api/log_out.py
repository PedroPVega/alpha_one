"""src/api/log_out.py"""

from fastapi import APIRouter, HTTPException, Response

from src.models import LogOutRequest, LogOutResponse

from src.core import handle_logout_request

log_out_router = APIRouter()

@log_out_router.post("/logout", response_model= LogOutResponse)
def log_out(payload: LogOutRequest):
    result: LogOutResponse | None = handle_logout_request(payload)
    if not result:
        raise HTTPException(status_code=500,
                            detail= "Internal server error")

    return result
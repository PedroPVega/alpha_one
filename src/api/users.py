"""src/api/users.py"""

from fastapi import APIRouter, HTTPException

from models import User, RefreshResponse, RefreshRequest

from core import handle_get_users, handle_refresh


users_router = APIRouter()

@users_router.get("/users", response_model = list[User])
def get_all_users():
    response: list[User] | None = handle_get_users()

    if not response:
        response = []

    return response

@users_router.post("/users/refresh", response_model = RefreshResponse)
def refresh_token(payload: RefreshRequest):
    response: RefreshResponse | None

    response = RefreshResponse(token = handle_refresh(payload.token))
    if not response:
        raise HTTPException(
            status_code=401,
            detail=""
        )

    return response

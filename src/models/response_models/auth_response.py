from pydantic import BaseModel

from models.users import User

class AuthResponse(BaseModel):
    user: User | None
    access_token: str
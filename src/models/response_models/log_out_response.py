from pydantic import BaseModel

class LogOutResponse(BaseModel):
    message: str
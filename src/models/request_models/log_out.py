from pydantic import BaseModel

class LogOutRequest(BaseModel):
    token: str
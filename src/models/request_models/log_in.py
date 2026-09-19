from pydantic import BaseModel

class LogInRequest(BaseModel):
    email: str = "default"
    password: str = "default"
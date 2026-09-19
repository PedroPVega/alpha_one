from pydantic import BaseModel

class SignUpRequest(BaseModel):
    pseudo: str = "default"
    email: str = "default"
    password: str = "default"
from pydantic import BaseModel

class RootResponse(BaseModel):
    message: str = "welcome to alpha one"
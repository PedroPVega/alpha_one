"""src/models/users/users.py"""

import uuid
import datetime

from typing import Literal

from pydantic import BaseModel, Field

class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    role: Literal["ADMIN", "USER"] = "USER"
    pseudo: str = "default"
    email: str = "default"
    favorite_number: int = 2
    prefered_theme: bool = True # False for dark

class UserPasswordPair(BaseModel):
    """Password Holder for a user generated at account creation
    
    Fields:
        hashed_password (string) : Hashed password for the given user
        user (User) : User to which the password belongs to"""
    hashed_password: str
    user: User

class SessionTokenHolder(BaseModel):
    """Session token holder created at the start of a client session.
    
    Fields:
        user_id (uuid) : The user's id to which this token belongs
        token (string) : The session token
        expirates (datetime) : The date and time at which this token expirates
        revoked (boolean) : Wether or not this token has been revoked of its validity"""
    user_id: uuid.UUID
    token: str
    expirates: datetime.datetime
    revoked: bool
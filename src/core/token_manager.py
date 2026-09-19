"""src/core/token_manager.py"""

import uuid
import datetime

from db import db

from models import SessionTokenHolder

from .security import generate_access_token

def handle_refresh(session_token: str) -> str | None:
    print("Handling refresh request")
    session_token_holder: SessionTokenHolder
    user_id: uuid.UUID
    access_token_generated: str | None = None

    try:
        session_token_holder = db.get_sessiontoken_by_value(session_token)
        user_id = session_token_holder.user_id
        if session_token_holder.revoked:
            print(f"Session token ****{session_token[-4:]} has been disabled")
        elif session_token_holder.expirates < datetime.datetime.now():
            print(f"Token {session_token} is expired")
        else:
            access_token_generated = generate_access_token(subject = str(user_id))
            print(f"Access token generated ****{access_token_generated[-4:]} with session token ****{session_token[-4:]}")

    except Exception as e:
        print(f"Unexpected exception while generating access token : {e}")

    return access_token_generated

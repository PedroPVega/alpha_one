"""src/core/security.py"""

import jwt
import bcrypt
import secrets
import datetime

from config import cfg
from models import User, SessionTokenHolder

ACCESS_TOKEN_LIFESPAN = 60 # duration of an access token in minutes

SESSION_TOKEN_SPAN = 4 # duration of a session token in hours

def hash_pw(password: str) -> str:
    result: str
    result = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    return result

def are_passwords_equal(true_hash: str, request_password: str) -> bool:

    return bcrypt.checkpw(request_password.encode(), true_hash.encode())


def generate_access_token(subject: str) -> str | None:
    # NOTE : all these should be env variables
    iat_timestamp: float = datetime.datetime.now()
    exp_timestamp: float = iat_timestamp + datetime.timedelta(minutes=ACCESS_TOKEN_LIFESPAN)
    headers = {"typ": cfg.jwt_alg}

    payload = {
        "sub" : subject,
        "exp": exp_timestamp,
        "iat": iat_timestamp
        }

    encoded_jwt = jwt.encode(payload=payload,
                             key=cfg.jwt_key,
                             algorithm=cfg.jwt_alg,
                             headers=headers)

    return encoded_jwt

def generate_session_token_for(user: User) -> SessionTokenHolder | None:
    session_token_holder: SessionTokenHolder
    expiration_time: datetime.datetime
    generated_token: str

    generated_token = secrets.token_urlsafe(24)
    expiration_time = datetime.datetime.now()
    expiration_time += datetime.timedelta(hours = SESSION_TOKEN_SPAN)
    try:
        session_token_holder = SessionTokenHolder(
            user_id = user.id,
            token = generated_token,
            expirates= expiration_time,
            revoked=False
        )
        print(f"Session token generated succesfully ****{generated_token[-4:]}")
            
    except Exception as e:
        session_token_holder = None
        print(f"Error while generating session token : {e}")

    return session_token_holder
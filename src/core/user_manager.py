"""src/core/user_manager.py"""
from db import db

from models import (SignUpRequest, LogInRequest, 
                    UserPasswordPair, User, 
                    SessionTokenHolder, AuthResponse, 
                    LogOutRequest, LogOutResponse)

from .security import hash_pw, are_passwords_equal, generate_access_token, generate_session_token_for

def handle_get_users() -> list[User]:
    print("Handling get users")

    user_list = []
    try:
        for pair in db.user_list:
            user_list.append(pair.user)
    except Exception as e:
        print(f"Error while recovering user list : {e}")

    return user_list


def handle_signup_request(user: SignUpRequest) -> tuple[AuthResponse, str] | None:
    print("Handling signup request")
    auth_response: AuthResponse | None
    retreived_user: User | None
    session_token: SessionTokenHolder
    wrapper: tuple[AuthResponse, str]
    access_token: str
    pw: str

    pw = hash_pw(user.password)
    retreived_user = db.add_user(user, pw)
    session_token = generate_session_token_for(retreived_user)
    access_token = generate_access_token(str(retreived_user.id))
    auth_response = AuthResponse(user=retreived_user, access_token=access_token)
    wrapper = (auth_response, session_token.token)

    db.add_session_token(session_token)
    pw = ""
    access_token = ""
    return wrapper

def handle_login_request(user: LogInRequest) -> tuple[AuthResponse, str] | None:
    print("Handling login request")
    auth_response: AuthResponse | None
    retreived_pair: UserPasswordPair | None
    wrapper: tuple[AuthResponse, str]
    session_token: SessionTokenHolder
    access_token: str

    retreived_pair = db.get_user_by_email(user.email)

    if retreived_pair is None:
        print("No matching user found !")
        wrapper = None

    elif are_passwords_equal(retreived_pair.hashed_password, user.password):
        print("Matching user found !")
        session_token = generate_session_token_for(retreived_pair.user)
        access_token = generate_access_token(str(retreived_pair.user.id))
        auth_response = AuthResponse(user=retreived_pair.user, access_token=access_token)
        wrapper = (auth_response, session_token.token)
        db.add_session_token(session_token)

    else:
        print("Password mismatch!")
        auth_response = None
        wrapper = None

    return wrapper

def handle_logout_request(request: LogOutRequest) -> LogOutResponse | None:
    response: LogOutResponse

    success = db.revoke_session_token(request.token)
    # NOTE : We could blacklist the jwt that is passed in the headers of the request

    if success:
        return LogOutResponse(message= "Logout was succesfull")

    else:
        return None
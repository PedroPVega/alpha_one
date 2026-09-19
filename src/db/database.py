"""Database.py"""

import uuid

from pydantic import BaseModel

from models import User, UserPasswordPair, SessionTokenHolder, SignUpRequest 

class DataBase(BaseModel):
    user_list: list[UserPasswordPair] = []
    session_tokens: list[SessionTokenHolder] = []

    ''' ====================== GETTERS ====================== '''
    def get_user_by_email(self, email: str) -> UserPasswordPair | None:
        # NOTE : this on a large scale, big dataset would take too long
        try:
            for pair in self.user_list:
                if email == pair.user.email:
                    return pair
            print("No user found with corresponding email")
        except Exception as e:
            print(f"Error while searching for user : {e}")

        return None

    def get_sessiontoken_by_value(self, session_token: str) -> SessionTokenHolder:
        # NOTE : this on a large scale, big dataset would take too long
        try:
            for session_token_holder in self.session_tokens:
                if session_token == session_token_holder.token:
                    return session_token_holder
            print("No corresponding session token found")
        except Exception as e:
            print(f"Error while searching for session token : {e}")
        
        return None

    def get_userid_by_session_token(self, session_token: str) -> uuid.UUID:
        session_token_holder: SessionTokenHolder

        try:
            session_token_holder = self.get_sessiontoken_by_value(session_token)
            return session_token_holder.user_id
        except Exception as e:
            print(f"Error while searching for user id: {e}")

        return None

    def get_session_token_status_by_value(self, session_token: str) -> bool:
        status: bool

        try:
            status = self.get_sessiontoken_by_value(session_token)
            
        except Exception as e:
            print(f"Error while searching for user : {e}")
            return None
        
        return status
    
    ''' ====================== ADDERS ====================== '''
    def add_user(self, request: SignUpRequest, hashed_pw: str) -> User | None:
        try:
            new_user: User | None = User(pseudo = request.pseudo,
                                  email = request.email,
            )
            user_password_pair: UserPasswordPair = UserPasswordPair(user = new_user,
                                                                    hashed_password = hashed_pw)
            self.user_list.append(user_password_pair)
            print("User created and added to the database !")
        except Exception as e:
            print(f"Error while adding new user to the database : {e}")
            new_user = None

        return new_user

    def add_session_token(self, session_token: SessionTokenHolder) -> SessionTokenHolder | None:
        try:
            self.session_tokens.append(session_token)
            print("Session token written into database")
                    
        except Exception as e:
            print(f"Error while writting into database : {e}")
            return None
        
        return session_token
    
    ''' ====================== PUTTERS ====================== '''
    def revoke_session_token(self, session_token: str):
        # NOTE : this on a large scale, big dataset would take too long
        success: bool = None

        try:
            for index in range (len(self.session_tokens)):
                if self.session_tokens[index].token == session_token:
                    self.session_tokens[index].revoked = True
                    success = True
                    print(f"Session token ****{session_token[-4:]} revocation for user {self.session_tokens[index].user_id} was successfull")
            if success is None:
                print(f"Token not found so revocation failed")
                success = False

        except Exception as e:
            print("Unexpected error at session token revocation : {e}")
            success = False

        return success



db = DataBase()
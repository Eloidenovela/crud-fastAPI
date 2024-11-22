from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def authenticate_user(username: str, password: str):
    try:
        from services.user import UserService
        from models.all import engine
        user_service = UserService(engine)
        user = user_service.verify_user({"username": username, "password": password})
       
        if user:
            return {
                "username": user.get("username"),
                "name": user.get("name"),
                "surname": user.get("surname"),
                "role": user.get("role")
            }
    
    except Exception as e:
        return e

async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + timedelta(minutes=30)
    else:
        expire = datetime.now() + timedelta(minutes=15)  # Tempo padrao de expiracao

    to_encode.update({"exp": expire})  # Adiciona a data de expiracao ao payload do token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Codifica o token JWT
    return encoded_jwt

def decode_token(token: str):
    from jwt.exceptions import DecodeError
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except DecodeError as e:
        return {"sub": None}
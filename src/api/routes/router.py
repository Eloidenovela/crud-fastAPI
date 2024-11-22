from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta
from api.middlewares.auth.auth_utils import (
    authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, 
    create_access_token
)

router = APIRouter()

@router.get("/", response_model=dict)
async def root():
    return {"root": "/"}

@router.post("/auth", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password) # funcao de autenticacao
   
    if user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # tempo de vida do token de acesso
        access_token = await create_access_token(
            data={"sub": form_data.username}, expires_delta=access_token_expires
        )

        return {
            "access_token": access_token, 
            "type": "bearer",
            "username": user.get("username"),
            "name": user.get("name"),
            "surname": user.get("surname"),
            "role": user.get("role")
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credencias Invalidas",
    )

from fastapi import APIRouter, Depends, HTTPException, status
from api.middlewares.auth.dependencies import get_current_user
from .schemas.user import UserCreate, UserUpdate, UserDelete

administration_router = APIRouter()

@administration_router.post("/admin/user/create", response_model=dict)
async def create_user(user: UserCreate, username: str=Depends(get_current_user)):
    from services.user import UserService
    from models.all import engine
    service = UserService(engine)
    current_user = service.get_by_username({"username": username})

    if (current_user.get("role") == "admin"):
        updated_user = service.create(user.to_json())
        return updated_user
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Apenas para o admin"
    )

@administration_router.put("/admin/user/update", response_model=dict)
async def create_user(user: UserUpdate, username: str=Depends(get_current_user)):
    from services.user import UserService
    from models.all import engine
    service = UserService(engine)
    current_user = service.get_by_username({"username": username})

    if (current_user.get("role") == "admin"):
        updated_user = service.update(user.to_json())
        return updated_user
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Apenas para o admin"
    )

@administration_router.delete("/admin/user/delete", response_model=dict)
async def delete_user(user: UserDelete, username: str=Depends(get_current_user)):
    from services.user import UserService
    from models.all import engine
    service = UserService(engine)
    current_user = service.get_by_username({"username": username})

    if current_user:
        if (current_user.get("role") == "admin"):
            deleted_user = service.delete(user.to_json())
            return deleted_user
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Apenas para o admin"
    )
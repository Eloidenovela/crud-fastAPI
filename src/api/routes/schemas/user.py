from pydantic import BaseModel
from models.enums.role import Role

class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    role: Role = Role.user

    def to_json(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "role": self.role.get_value()
        }
    
class UserUpdate(BaseModel):
    id: int
    username: str = None
    password: str = None
    name: str = None
    surname: str = None
    role: Role = Role.user

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "role": self.role.get_value()
        }
    
class UserDelete(BaseModel):
    id: int
    def to_json(self):
        return {
            "id": self.id
        }
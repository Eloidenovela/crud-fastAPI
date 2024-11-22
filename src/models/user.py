from .all import engine
from sqlalchemy.ext.declarative import declarative_base
from .enums.role import Role
from sqlalchemy import Enum as PgEnum
from sqlalchemy import (
    Column, String, Integer
)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    role = Column(PgEnum(Role, name="role"), nullable=False, default=Role.user)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "role": self.role.get_value()
        }

    @classmethod
    def to_model(cls, __username, __password, __name, __surname, __role: Role):
        return cls(
            username=__username,
            password=__password,
            name=__name,
            surname=__surname,
            role=__role
        )
    
def create_table():
    Base.metadata.create_all(engine)
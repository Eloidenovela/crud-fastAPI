from .service import Service
from sqlalchemy.orm import Session
from models.user import User

class UserService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            from models.enums.role import Role
            try:
                created_user = User.to_model(
                    data.get("username"),
                    data.get("password"),
                    data.get("name"),
                    data.get("surname"),
                    Role(data.get("role"))
                )

                session.add(created_user)
                session.commit()
                return created_user.to_json()
            
            except Exception as e:
                session.rollback()
                return e
            
    def update(self, data):
        with Session(self.engine) as session:
            try:
                updated_user = session.query(User).filter(User.id == data.get("id")).first()
                if updated_user:
                    for key, value in data.items():
                        if (hasattr(updated_user, key)):
                            if value:
                                setattr(updated_user, key, value)
                    session.commit()
                    return updated_user.to_json()
                return {"response": "not found"}
            except Exception as e:
                session.rollback()
                return e
    
    def delete(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import delete
                delete_query = delete(User).where(User.id == data.get("id"))
                result = session.execute(delete_query)
                session.commit()
                if result.rowcount > 0:
                    return {"response": "ok"}
                
                return {"response": "not found"}
            except Exception as e:
                session.rollback()
                return e
            
    def get_all(self):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import select
                query = select(User)
                result = session.execute(query).scalars().all()
                users = [user.to_json() for user in result]
                return users
            except Exception as e:
                return e
    
    def get_by_id(self, data):
        with Session(self.engine) as session:
            user = session.query(User).filter(User.id == data.get("id")).first()
            if user:
                return user.to_json()

    def get_by_username(self, data):
        with Session(self.engine) as session:
            user = session.query(User).filter(User.username.like(data.get("username"))).first()
            if user:
                return user.to_json()
        
    def verify_user(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import and_
            user = session.query(User).filter(
                and_(
                    User.username.like(data.get("username")),
                    User.password.like(data.get("password"))
                )
            ).first()
            if user:
                return user.to_json()

            

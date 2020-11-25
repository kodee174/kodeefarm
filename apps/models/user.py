import enum
from sqlalchemy import *
from apps.models import Base, session

class User(Base):
    
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def __init__(self):
        self.query = session.query(User)

    def auth(self, username_or_email, password):
        user = self.query.filter(
            or_(
                User.username==username_or_email, 
                User.email==username_or_email
            ),
            User.password==password
        ).first()
        if user:
            return user
        return None

    
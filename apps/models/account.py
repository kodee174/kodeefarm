from sqlalchemy import *
from apps.models import Base, session


class Account(Base):
    
    __tablename__ = 'account'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def __init__(self):
        self.query = session.query(Account)

    def create(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        session.add(self)
        session.commit()

    def update(self):
        pass
    
    def delete(self):
        pass

    def get(self, id):
        return self.query.get(id)

    def get_all(self):
        return self.query.all()

    def auth(self, username, password):
        account = self.query.filter(username==username, password==password).first()
        if account:
            return account
        return False

    
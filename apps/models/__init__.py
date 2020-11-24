from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///apps/configs/data.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

from apps.models.account import Account

Base.metadata.create_all(engine)
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///riddle.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    answers = Column(Integer)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password, answers):
        """"""
        self.username = username
        self.password = password
        self.answers = answers
 
# create tables
Base.metadata.create_all(engine)


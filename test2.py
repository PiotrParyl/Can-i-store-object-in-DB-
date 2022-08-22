from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from random import choice
from string import letters

engine = create_engine('sqlite:////tmp/teste.db', echo=True)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(40))
    address = Column(UnicodeText, nullable=True)
    password = Column(String(20))

    def __init__(self, name, address=None, password=None):
        self.name = name
        self.address = address
        if password is None:
            password = ''.join(choice(letters) for n in xrange(10))
        self.password = password

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
s = Session()
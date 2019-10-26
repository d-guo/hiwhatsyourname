from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///userinfo.db', echo=True)
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = "userinfo"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    facebook = Column(String)
    pic = 
 
    def __repr__(self):
        return "{}".format(self.name)

 
# create tables
Base.metadata.create_all(engine)
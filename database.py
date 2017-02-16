from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
	__tablename__= 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	email = Column(String(255))
	mailaddress = Column(String(255))
	password = Column(String(255))
	user = relationship("User", back_populates ="user")

class Recipe(Base):	
	__tablename__= 'recipe'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	title = Column(String(255))
	description = Column(String(255))
	nationality = Column(String(255))
	user = relationship("User", back_populates ="recipe")
	history = Column(String(255))

class Order(Base):
	__tablename__='order'
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	mailaddress = Column(String(255))
	user = relationship("User", back_populates ="order")

engine = create_engine('sqlite:///tastepal.db')

Base.metadata.create_all(engine)










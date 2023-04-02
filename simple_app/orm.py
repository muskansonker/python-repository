from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime as dt

Base=declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id=Column(Integer, primary_key=True)
    name=Column(String(50))

    def __str__(self) -> str:
        return self.name

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    category=Column(Integer, ForeignKey('categories.id'))
    created_on=Column(DateTime, default=dt.now)

if __name__ == '__main__': # if this file is run directly 
    engine=create_engine('sqlite:///db.sqlite',echo=True)
    Base.metadata.create_all(engine)

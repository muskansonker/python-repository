from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Float,String,DateTime,ForeignKey

Base=declarative_base()

class Image(Base):
    __tablename__='images'
    id=Column(Integer, primary_key=True)
    image_name=Column(String(50))
    size=Column(Float)

if __name__ == '__main__':
    engine=create_engine('sqlite:///db.sqlite',echo=True)
    Base.metadata.create_all(engine)

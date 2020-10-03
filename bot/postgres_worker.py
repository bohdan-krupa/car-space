import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String, Date, REAL, Text


Base = declarative_base()
engine = create_engine("postgresql://postgres@localhost:5431/postgres")

class Parking(Base):
    __tablename__ = "parking"
    id = Column(Integer(), primary_key=True)
    street = Column(String())
    latitude = Column(REAL())
    longitude = Column(REAL())
    camera_url = Column(Text())

    def datafromJson(self):
        pass


Base.metadata.create_all(engine)












    print(records)
except Exception as e:
    print(e)
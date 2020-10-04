import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String, Date, REAL, Text, BOOLEAN


Base = declarative_base()
engine = create_engine("postgresql://postgres@localhost:5431/postgres")

class Parking(Base):
    __tablename__ = "parking"
    id = Column(Integer(), primary_key=True)
    street = Column(String())
    spaces_amount = Column(Integer())
    latitude = Column(REAL())
    longitude = Column(REAL())
    camera_url = Column(BOOLEAN())

    @staticmethod
    def datafromJson():
        with open("./backupData/SQLite.json", "r") as file:
            data = json.loads(file.read())
        
        for i in data:
            parking = Parking(
                    id=i.get('id'), 
                    street=i.get('street'), 
                    spaces_amount=i.get('spaces_amount'),
                    latitude=i.get('latitude'),
                    longitude=i.get('longitude'),
                    camera_url=i.get('is_camera')
                    )
            


Parking.datafromJson()
Base.metadata.create_all(engine)












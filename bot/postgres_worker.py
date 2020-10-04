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
        
        values = [list(x.values()) for x in data]
        print(values)

                



            
                
                
           

        
Parking.datafromJson()
Base.metadata.create_all(engine)












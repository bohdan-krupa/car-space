import json
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String, Date, REAL, Text, BOOLEAN, Table



Base = declarative_base()
engine = create_engine("postgresql://postgres@localhost:5431/postgres")

try:
    conn = psycopg2.connect(dbname='postgres', 
                            user='postgres', 
                            password='',
                            host='localhost',
                            port='5431'
                            )
except Exception as e:
    print(e)

class SQL:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor()


    def __del__(self):
        self.conn.close()


#   def set_spaces_amount(self, id, spaces_amount):
#     with self.connection:
#       query = f'UPDATE parkings SET spaces_amount = ? WHERE id = ?'
#       self.cursor.execute(query, (spaces_amount, id))


    def get_parkings(self):
        with self.connection:
            query = f'SELECT * FROM _parkings'
            return self.cursor.execute(query).fetchall()






# class Parking(Base):
#     __tablename__ = Table('_subscriptions', Base.metadata,
#                     autoload=True, autoload_with=engine)


            


# parking = Parking()
# parking.datafromJson()
# Base.metadata.create_all(engine)












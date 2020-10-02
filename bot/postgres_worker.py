import psycopg2

try:
    con = psycopg2.connect(
        database="car-parking",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5432"
    )mrRobot2205
except Exception as e:
    print(e)


import psycopg2

try:
    conn = psycopg2.connect(
        database="krp",
        user="postgres",
        password="",
        host="127.0.0.1",
        port="5431"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts;")
    records = cursor.fetchall()

    print(records)
except Exception as e:
    print(e)
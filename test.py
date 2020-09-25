import csv
import sqlite3

connection = sqlite3.connect('parkings.db')
cursor = connection.cursor()

# Open file and read its content into database
with open("park.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("INSERT INTO parkings VALUES (?, ?, ?, ?, ?, ?)", (row["id"], row["name"], row["spaces_amount"], row["latitude"], row["longitude"], row["is_camera"]))

connection.commit()

connection.close()
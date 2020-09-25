import sqlite3


class SQL:
  def __init__(self):
    self.connection = sqlite3.connect('parkings.db')
    self.cursor = self.connection.cursor()


  def __del__(self):
    self.connection.close()


  def set_spaces_amount(self, id, spaces_amount):
    with self.connection:
      query = f'UPDATE parkings SET spaces_amount = ? WHERE id = ?'
      self.cursor.execute(query, (spaces_amount, id))


  def get_all_parkings(self):
    with self.connection:
      query = f'SELECT * FROM parkings'
      return self.cursor.execute(query).fetchall()
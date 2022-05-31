import mysql.connector
from pygame import Cursor

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()
mycursor.execute()
myresult = mycursor.fetchall()
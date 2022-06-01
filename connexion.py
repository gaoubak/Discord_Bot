import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  db="pokedex"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pokemon where nom_pok = 'pikachu' ")
myresult = mycursor.fetchall()
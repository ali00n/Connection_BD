import mysql.connector

from aula136 import mycursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= "mydatabase"
)

mycursor = mydb.cursor()

# sql ="ALTER TABLE Alunos drop column id"

sql = "ALTER TABLE Alunos add id int first"

mycursor.execute(sql)

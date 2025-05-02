import mysql.connector

from aula137 import mycursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

sql = ""

mycursor.execute(sql)
import mysql.connector

from aula136 import mycursor

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "root",
    database = "mydb"
)


mycursor = mydb.cursor()

sql = """create table pessoas(
nome varchar(255)
idade int (2))"""


mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)



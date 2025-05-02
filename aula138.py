import mysql.connector

from aula137 import mycursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# sql = "alter table Alunos ADD sobrenome varchar(255)"

# sql ="Alter table Alunos drop sobrenome"

#sql = "ALTER TABLE Alunos ADD sobrenome VARCHAR(255) AFTER nome"

#sql = "ALTER TABLE Alunos DROP COLUMN sobrenome"


mycursor.execute(sql)
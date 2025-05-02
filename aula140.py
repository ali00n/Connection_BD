import mysql.connector
from mysql.connector import Error
from aula137 import mycursor

try:
    sql = ("INSERT INTO Alunos (id, nome, sobrenome, idade)"
           " VALUES (1, 'Gabriel', 'Artigas', '36')")
    mycursor.execute(sql)

    print("Dados inseridos com sucesso!")
except Error as err:
    print(f"Erro ao inserir dados: {err}")

sql_select = "SELECT * FROM Alunos"
mycursor.execute(sql_select)
for aluno in mycursor.fetchall():
    print(aluno)



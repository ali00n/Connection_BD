import mysql.connector
from aula138 import mydb

mycursor = mydb.cursor()

# sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, 'Gabriel', 'Artigas', 36)"

sql = "INSERT INTO Alunos (id, nome, sobrenome, idade) VALUES (NULL, %s, %s, %s)"

# val = ("Danny", "Logan", "35")
# mycursor.execute(sql, val)
val = [
    ("Arthur", "Logan", "18"),
    ("Lucas", "Thuxs", "17"),
    ("Beatriz", "Silva", "24"),
    ("João", "Maciel", "52")
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "registros inseridos")
print(mycursor.lastrowid)
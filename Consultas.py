import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Alisson",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Alunos")

print("\n=== alunos cadastrados: ")
for (id, Nome, Email) in mycursor:
    print(f"ID: {id}, Nome: {Nome}, Email: {Email}")
mycursor.close()
mydb.close()
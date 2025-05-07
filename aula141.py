import mysql.connector
from mysql.connector import Error

try:
    # Conectando ao banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    if mydb.is_connected():
        print("Conexão bem-sucedida!")


        mycursor = mydb.cursor()

        sql = "SELECT * FROM Alunos"
        mycursor.execute(sql)

        resultados = mycursor.fetchall()
        for linha in resultados:
            print(linha)

except Error as e:
    print(f"Erro durante a conexão ou operação: {e}")

finally:
    # Fechando a conexão, mesmo se houver erro
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("\nConexão encerrada.")

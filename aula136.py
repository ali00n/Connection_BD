import mysql.connector
from mysql.connector import Error



try:
    # Conectando ao banco de dados
    mydb = mysql.connector.connect(
        host="localhost",
        user="Alisson",
        password="abc123",
        database="mydatabase"
    )

    if mydb.is_connected():
        print("Conexão bem-sucedida!")

        # Criando um cursor
        mycursor = mydb.cursor()

        # Criando a tabela 'alunos'
        sql = """CREATE TABLE IF NOT EXISTS alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL,
            curso VARCHAR(255) NOT NULL
        )"""
        mycursor.execute(sql)
        print("Tabela 'alunos' criada ou já existente.")

        # Listar todas as tabelas no banco (opcional)
        mycursor.execute("SHOW TABLES")
        tabelas = mycursor.fetchall()
        print("\nTabelas no banco de dados:")
        for tabela in tabelas:
            print(tabela[0])



except Error as e:
    print(f"Erro durante a conexão ou operação: {e}")

finally:
    # Fechando a conexão, mesmo se houver erro
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("\nConexão encerrada.")
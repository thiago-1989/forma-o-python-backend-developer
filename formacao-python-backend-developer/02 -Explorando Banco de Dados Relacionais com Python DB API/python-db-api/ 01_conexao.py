import sqlite3
import mysql.connector
from pathlib import Path 

ROOT_PATH = Path(__file__).parent
"""
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
print(conexao)
cur = conexao.cursor()

cur.execute("")
"""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="backend_dio",
)

cursor = mydb.cursor()

def criar_tabela(mydb, cursor, nome):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes(id int PRIMARY KEY AUTO_INCREMENT, "
        "nome VARCHAR(100), email varchar(150))")
    mydb.commit()

def inserir_registro(mydb, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s);", data)
    mydb.commit()

def atualiza_registro(mydb, cursor, nome, email, id):
    data = (nome, email, id)
    try:
        cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s;", data)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Erro")
def remover_registro(mydb, cursor, id):
    data = (id,)
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s;", data)
        mydb.commit()  # Confirma a alteração no banco de dados
        print(f"Registro com ID {id} removido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao remover registro: {err}")


atualiza_registro(mydb, cursor, "Thiago Oliveira", "thiago@gmail.com", 1)
remover_registro(mydb, cursor, 1)
"""Commit"""
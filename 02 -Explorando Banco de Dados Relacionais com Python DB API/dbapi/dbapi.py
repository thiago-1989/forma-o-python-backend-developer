import sqlite3
import mysql.connector
from pathlib import Path
from dulwich.porcelain import fetch

# Define o caminho raiz do projeto com base no arquivo atual
ROOT_PATH = Path(__file__).parent

"""
Trecho comentado para conexão com um banco SQLite (não utilizado atualmente):
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
print(conexao)
cur = conexao.cursor()
cur.execute("")
"""

# Conexão com o banco de dados MySQL
mydb = mysql.connector.connect(
    host="localhost",  # Endereço do servidor MySQL
    user="root",       # Nome do usuário do banco de dados
    passwd="",         # Senha do usuário (atualmente em branco)
    database="backend_dio",  # Nome do banco de dados utilizado
)

# Cursor para executar operações no banco de dados
cursor = mydb.cursor()

# Função para criar a tabela 'clientes', se ela não existir
def criar_tabela(mydb, cursor, nome):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes(id int PRIMARY KEY AUTO_INCREMENT, "
        "nome VARCHAR(100), email varchar(150))"
    )
    mydb.commit()  # Confirma a criação da tabela no banco de dados

# Função para inserir um registro na tabela 'clientes'
def inserir_registro(mydb, cursor, data):
    cursor.execute(
        "INSERT INTO IF NOT EXISTS clientes (nome, email) VALUES (%s, %s);", data
    )  # Insere os dados no formato especificado
    mydb.commit()  # Confirma a inserção no banco de dados

# Função para atualizar um registro na tabela 'clientes' com base no ID
def atualiza_registro(mydb, cursor, nome, email, id):
    data = (nome, email, id)  # Dados a serem atualizados
    try:
        cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s;", data)
        mydb.commit()  # Confirma a atualização no banco de dados
    except mysql.connector.Error as err:
        print("Erro")  # Mensagem de erro em caso de falha

# Função para remover um registro da tabela 'clientes' com base no ID
def remover_registro(mydb, cursor, id):
    data = (id,)  # ID do registro a ser removido
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s;", data)
        mydb.commit()  # Confirma a remoção no banco de dados
        print(f"Registro com ID {id} removido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao remover registro: {err}")  # Mensagem de erro em caso de falha

# Função para inserir vários registros na tabela 'clientes'
def inserir_muitos(mydb, cursor, data):
    try:
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (%s, %s);", data)
        mydb.commit()  # Confirma as inserções no banco de dados
        print(f"Registro com dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        print("Erro")  # Mensagem de erro em caso de falha

# Função para recuperar um cliente da tabela 'clientes' com base no ID
def recuperar_cliente(mydb, cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = %s;", (id,))
    registro = cursor.fetchone()  # Recupera o primeiro registro encontrado
    return registro

# Função para listar todos os clientes da tabela 'clientes' em ordem alfabética
def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY id ASC;")
    registros = cursor.fetchall()  # Recupera todos os registros encontrados
    return registros
"""
data = [("Adamastor", "adm@gmail.com"), ("Margarethi", "mg@gmail.com"), ("thiago", "th@gmail.com")]

inserir_muitos(mydb, cursor, data)

data = (recuperar_cliente(mydb, cursor, 2))

clientes = listar_clientes(cursor)

for registro in clientes:
    print(registro)
"""

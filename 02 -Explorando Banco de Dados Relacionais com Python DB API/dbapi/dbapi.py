import sqlite3
import mysql.connector
from pathlib import Path

# Define o caminho raiz do projeto com base no arquivo atual
ROOT_PATH = Path(__file__).parent

# Conexão com um banco SQLite (não utilizado atualmente)
sqlite = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
# Cursor para executar operações no banco de dados sqlite
cursor_sqlite = sqlite.cursor()

# Conexão com o banco de dados MySQL
"""mydb = mysql.connector.connect(
    host="localhost",  # Endereço do servidor MySQL
    user="root",       # Nome do usuário do banco de dados
    passwd="",         # Senha do usuário (atualmente em branco)
    database="backend_dio",  # Nome do banco de dados utilizado
)
# Cursor para executar operações no banco de dados MySQL
cursor_mysql = mydb.cursor()
"""

# Função para criar a tabela 'clientes' no MySQL, se ela não existir
def criar_tabela_mysql(mydb, cursor_mysql):
    cursor_mysql.execute(
        "CREATE TABLE IF NOT EXISTS clientes(id int PRIMARY KEY AUTO_INCREMENT, "
        "nome VARCHAR(100), email varchar(150))"
    )
    mydb.commit()  # Confirma a criação da tabela no banco de dados MySQL

# Função para criar a tabela 'clientes' no SQLite, se ela não existir
def criar_tabela_sqlite(sqlite, cursor_sqlite):
    cursor_sqlite.execute(
        "CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome VARCHAR(100), email varchar(150))"
    )
    sqlite.commit()  # Confirma a criação da tabela no banco de dados SQLite

# Função para inserir um registro na tabela 'clientes'
def inserir_registro_mysql(mydb, cursor, data):
    cursor.execute(
        "INSERT INTO IF NOT EXISTS clientes (nome, email) VALUES (%s, %s);", data
    )  # Insere os dados no formato especificado
    mydb.commit()  # Confirma a inserção no banco de dados

# Função para inserir um registro na tabela 'clientes' no SQLite 
def inserir_registro_sqlite(sqlite, cursor_sqlite, data): 
    # Insere os dados no formato especificado 
    cursor_sqlite.execute( "INSERT INTO clientes (nome, email) VALUES (?, ?);", data ) 
    # Confirma a inserção no banco de dados
    sqlite.commit() 

# Função para atualizar um registro na tabela 'clientes' com base no ID
def atualiza_registro_mysql(mydb, cursor, nome, email, id):
    data = (nome, email, id)  # Dados a serem atualizados
    try:
        cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s;", data)
        mydb.commit()  # Confirma a atualização no banco de dados
    except mysql.connector.Error as err:
        print("Erro")  # Mensagem de erro em caso de falha

 # Função para atualizar um registro na tabela 'clientes' no SQLite com base no ID 
def atualiza_registro_sqlite(sqlite, cursor_sqlite, nome, email, id):  
    # Dados a serem atualizados 
    data = (nome, email, id)
    try: 
        cursor_sqlite.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", data)  
    except sqlite3.Error as err:  
        # Mensagem de erro em caso de falha
        print("Erro")
    # Confirma a atualização no banco de dados 
    sqlite.commit()

# Função para remover um registro da tabela 'clientes' com base no ID
def remover_registro_mysql(mydb, cursor, id):
    # ID do registro a ser removido
    data = (input("Id a ser removido: "),) 
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s;", data)
        mydb.commit()  # Confirma a remoção no banco de dados
        print(f"Registro com ID {id} removido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao remover registro: {err}")  # Mensagem de erro em caso de falha

# Função para remover um registro da tabela 'clientes' no SQLite com base no ID 
def remover_registro_sqlite(sqlite, cursor_sqlite): 
    # ID do registro a ser removido 
    data = (input("Id a ser removido: "),) 
    try: 
        cursor_sqlite.execute("DELETE FROM clientes WHERE id = ?;", data) 
        sqlite.commit() # Confirma a remoção no banco de dados 
        print(f"Registro com ID {id} removido com sucesso!") 
    except sqlite3.Error as err: 
        print(f"Erro ao remover registro: {err}") # Mensagem de erro em caso de falha

# Função para inserir vários registros na tabela 'clientes'
def inserir_muitos_mysql(mydb, cursor_mysql):
    data = []
    try:
        # Laço para inserir um número indefinido de registros 
        while True: 
            nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ") 
            if nome.lower() == 'sair': 
                break 
            email = input("Digite o email do cliente: ") 
            insercao = (nome, email) 
            data.append(insercao)
                
        cursor_mysql.executemany("INSERT INTO clientes (nome, email) VALUES (%s, %s);", data)
        mydb.commit()  # Confirma as inserções no banco de dados
        print(f"Registro com dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        print("Erro")  # Mensagem de erro em caso de falha

# Função para inserir vários registros na tabela 'clientes' no SQLite 
def inserir_muitos_sqlite(sqlite, cursor_sqlite):
    data = []
    try:
        continuar = "sim"
        # Laço para inserir um número indefinido de registros 
        while continuar == "sim": 
            nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ") 
            email = input("Digite o email do cliente: ") 
            insercao = (nome, email) 
            data.append(insercao)
            continuar = input("Continuar inserção? \n")    
        cursor_sqlite.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
        sqlite.commit()  # Confirma as inserções no banco de dados
        print(f"Registro com dados inseridos com sucesso!")
    except sqlite3.Error as err: 
        print(f"Erro ao remover registro: {err}") # Mensagem de erro em caso de falha 

# Função para recuperar um cliente da tabela 'clientes' com mysql baseado no ID
def recuperar_cliente_mysql(cursor_mysql):
    while True:
        id = input("Digite o Id ou fim: ")
        if id.lower == "fim":
            break              
        cursor_mysql.execute("SELECT * FROM clientes WHERE id = %s;", (id,))
        registro = cursor_mysql.fetchone()  # Recupera o primeiro registro encontrado
        return registro

# Função para recuperar um cliente da tabela 'clientes' com sqlite baseado no ID
def recuperar_cliente_sqlite(cursor_sqlite):
    while True:
        id = input("Digite o Id ou fim: ")
        if id.lower == "fim":
            break              
        cursor_sqlite.execute("SELECT * FROM clientes WHERE id = %s;", (id,))
        registro = cursor_sqlite.fetchone()  # Recupera o primeiro registro encontrado
        return registro
    
# Função para listar todos os clientes da tabela 'clientes' em ordem alfabética no mysql
def listar_clientes_mysql(cursor_mysql):
    cursor_mysql.execute("SELECT * FROM clientes ORDER BY id ASC;")
    registros = cursor_mysql.fetchall()  # Recupera todos os registros encontrados
    return registros

# Função para listar todos os clientes da tabela 'clientes' em ordem alfabética no sqlite
def listar_clientes_sqlite(cursor_mysql):
    cursor_sqlite.execute("SELECT * FROM clientes ORDER BY id ASC;")
    registros = cursor_sqlite.fetchall()  # Recupera todos os registros encontrados
    return registros

# Chamando as funções para criar as tabelas (se necessário)
criar_tabela_sqlite(sqlite, cursor_sqlite)
inserir_muitos_sqlite(sqlite, cursor_sqlite)

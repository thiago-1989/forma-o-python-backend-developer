import sqlite3
from dbapi.util import *

# Argumentos DB mysql
host="localhost"            # Endereço do servidor MySQL
user="root"                 # Nome do usuário do banco de dados
passwd=""                   # Senha do usuário (atualmente em branco)
database="backend_dio"      # Nome do banco de dados utilizado

# Conectando aos bancos de dados
#conexao_mysql = conectar_mysql(host, user, passwd, database)

db_sqlite = "../dbapi/meu_banco.sqlite"
conexao_sqlite = sqlite3.connect(db_sqlite)

# Cursor para executar operações no banco de dados sqlite
cursor_sqlite = conexao_sqlite.cursor()

# Cursor para executar operações no banco de dados MySQL
#cursor_mysql = conexao_mysql.cursor()

# Executando a consulta e armazenando os resultados
tabela = cursor_sqlite.execute("SELECT * FROM clientes")
resultados = tabela.fetchall()

# Imprimindo os resultados
for linha in resultados:
    print(linha)

import mysql.connector

# Argumentos DB mysql
host="localhost"            # Endereço do servidor MySQL
user="root"                 # Nome do usuário do banco de dados
passwd=""                   # Senha do usuário (atualmente em branco)
database="backend_dio"      # Nome do banco de dados utilizado

# Conectando aos bancos de dados
conexao_mysql = mysql.connector.connect(
        host=host,
        user=user,
        password=passwd,
        database=database
    )

# Cursor para executar operações no banco de dados MySQL
cursor_mysql = conexao_mysql.cursor()

#db_sqlite = "../dbapi/meu_banco.sqlite"
#conexao_sqlite = sqlite3.connect(db_sqlite)

# Cursor para executar operações no banco de dados sqlite
#cursor_sqlite = conexao_sqlite.cursor()

# Cursor para executar operações no banco de dados MySQL
cursor_mysql = conexao_mysql.cursor()

# Executando a consulta e armazenando os resultados
cursor_mysql.execute("SELECT * FROM clientes")
resultados = cursor_mysql.fetchall()

# Imprimindo os resultados
for linha in resultados:
    print(linha)

"""    
# Executando a consulta e armazenando os resultados
tabela = cursor_mysql.execute("SELECT * FROM clientes")
resultados = tabela.fetchall()

# Imprimindo os resultados
for linha in resultados:
    print(linha)
"""
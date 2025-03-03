import os
import click
from flask import Flask, current_app  # Importa a classe Flask para criar a aplicação web
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')

def create_app(test_config=None):
    # Cria e configura a aplicação Flask
    app = Flask(__name__, instance_relative_config=True)

    # Define a configuração padrão da aplicação
    app.config.from_mapping(
        SECRET_KEY='dev',  # Chave secreta utilizada para manter os dados seguros (ideal usar outra chave em produção)
        SQLALCHEMY_DATABASE_URI="sqlite:///diobank.sqlite",  # Caminho do arquivo do banco de dados SQLite
    )

    if test_config is None:
        # Carrega a configuração da instância (config.py), se existir e não estiver em modo de teste
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração de teste, se passada como argumento
        app.config.from_mapping(test_config)

    # Define uma rota simples que retorna "Hello, World!" ao acessar /hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.cli.add_command(init_db_command)
    db.init_app(app)

    return app  # Retorna a aplicação configurada

from flask import Flask  # Importa a classe Flask para criar a aplicação web

def create_app(test_config=None):
    # Cria e configura a aplicação Flask
    app = Flask(__name__, instance_relative_config=True)

    # Define a configuração padrão da aplicação
    app.config.from_mapping(
        SECRET_KEY='dev',  # Chave secreta utilizada para manter os dados seguros (ideal usar outra chave em produção)
        DATABASE='diobank.sqlite',  # Caminho do arquivo do banco de dados SQLite
    )

    if test_config is None:
        # Carrega a configuração da instância (config.py), se existir e não estiver em modo de teste
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração de teste, se passada como argumento
        app.config.from_mapping(test_config)

    # Garante que a pasta de instância exista
    try:
        os.makedirs(app.instance_path)  # Cria a pasta de instância se ela não existir
    except OSError:
        pass  # Ignora o erro se a pasta já existir

    # Define uma rota simples que retorna "Hello, World!" ao acessar /hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db

    db.init_app(app)

    return app  # Retorna a aplicação configurada

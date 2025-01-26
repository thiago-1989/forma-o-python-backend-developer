from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/hello/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        return {
            "message": "Olá, dev! Você fez uma requisição POST"
        }
    else:
        return {
            "message": "Olá, dev! Você fez uma requisição GET"
        }
@app.route("/welcome/<usuario>/<int:idade>/<string:email>")
def welcome(usuario, idade, email):
    return {
        "Message": "Seja bem-vindo!",
        "Nome": usuario,
        "Idade": idade,
        "Email": email
    }

with app.test_request_context():
    print(url_for("hello"))
    print(url_for("hello", next="/"))
    print(url_for("welcome", usuario="Thiago Oliveira", idade=35, email="<thiagoliveira@gmail.com>"))
    
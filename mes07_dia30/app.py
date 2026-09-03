from flask import Flask
from controllers.aluno_controller import aluno_controller

def criar_aplicacao():
    app = Flask(__name__)

    app.register_blueprint(aluno_controller)

    return app

app = criar_aplicacao()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

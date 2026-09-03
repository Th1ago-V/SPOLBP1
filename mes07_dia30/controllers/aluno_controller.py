from flask import Blueprint, render_template, request, redirect, url_for
from models.aluno import Aluno
from services.aluno_validator import AlunoValidator

aluno_controller = Blueprint(
    "aluno_controller",
    __name__
)

alunos_cadastrados = []

@aluno_controller.route("/")
def inicio():
    return redirect(url_for("aluno_controller.formulario"))

@aluno_controller.route(
    "/alunos/novo",
    methods=["GET", "POST"]
)
def formulario():
    dados = {
        "nome": "",
        "email": "",
        "idade": "",
        "curso": ""
    }

    erros = {}

    if request.method == "POST":
        dados = {
            "nome": request.form.get("nome", ""),
            "email": request.form.get("email", ""),
            "idade": request.form.get("idade", ""),
            "curso": request.form.get("curso", "")
        }

        erros = AlunoValidator.validar(dados)

        if not erros:
            aluno = Aluno(
                nome=dados["nome"].strip(),
                email=dados["email"].strip(),
                idade=int(dados["idade"]),
                curso=dados["curso"]
            )

            alunos_cadastrados.append(aluno)

            return redirect(
                url_for("aluno_controller.listar")
            )

    return render_template(
        "formulario.html",
        dados=dados,
        erros=erros
    )

@aluno_controller.route("/alunos")
def listar():
    return render_template(
        "lista.html",
        alunos=alunos_cadastrados
    )

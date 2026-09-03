import re

class AlunoValidator:
    @staticmethod
    def validar(dados):
        erros = {}

        nome = dados.get("nome", "").strip()
        email = dados.get("email", "").strip()
        idade = dados.get("idade", "").strip()
        curso = dados.get("curso", "").strip()

        if not nome:
            erros["nome"] = "O nome é obrigatório."
        elif len(nome) < 3:
            erros["nome"] = "O nome deve possuir pelo menos 3 caracteres."

        if not email:
            erros["email"] = "O e-mail é obrigatório."
        elif not AlunoValidator.email_valido(email):
            erros["email"] = "Digite um endereço de e-mail válido."

        if not idade:
            erros["idade"] = "A idade é obrigatória."
        else:
            try:
                idade_numero = int(idade)

                if idade_numero < 14 or idade_numero > 100:
                    erros["idade"] = (
                        "A idade deve estar entre 14 e 100 anos."
                    )
            except ValueError:
                erros["idade"] = "A idade deve ser um número inteiro."

        cursos_validos = [
            "Informática",
            "Administração",
            "Eletrônica",
            "Mecânica"
        ]

        if not curso:
            erros["curso"] = "Selecione um curso."
        elif curso not in cursos_validos:
            erros["curso"] = "O curso selecionado não é válido."

        return erros

    @staticmethod
    def email_valido(email):
        padrao = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return re.match(padrao, email) is not None

class Aluno:
    def __init__(self, nome, email, idade, curso):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.curso = curso

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade,
            "curso": self.curso
        }

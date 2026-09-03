from model.usuario import Usuario
from model.livro import Livro

from view.login_view import LoginView
from view.livro_view import LivroView

# Cria tabelas
Usuario.criar_tabela()
Livro.criar()

# Cadastro inicial de usuário
print("\n=== CADASTRO DE USUÁRIO===")

login = input("Novo usuaário: ")
senha = input("Senha: ")

Usuario.cadastrar(login,senha)

# Login
print("\n=== LOGIN ===")

login, senha == LoginView.exibir()

usuario = LoginController.autenticar(login, senha)

if usuario:
	print("\nLogin realizado.\n")
	while True:
		opcao = LivroView.menu()
		if opcao == "1":
			LivroController.cadastrar()
		elif opcao == "2":
			livros = Livro.consultar()
			print("\n=== LIVROS ===")
			for l in livros:
				print(l)
		elif opcao == "3":
			id_livro = int(input("ID do livro para excluir: "))
			Livro.excluir(id_livro)
			print("Livro removido.")
		elif opcao == "4":
			Livro.exportar()
		elif opcao == "0":
			print("Encerrando...")
		else:
			("Opção inválida.")
else:
	print("Usuário ou senha incorretos.")

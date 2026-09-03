from model.usuario_model import Usuario
from model.produto_model import Produto

from view.login_view import LoginView
from view.produto_view import ProdutoView

from controller.login_controller import LoginController
from controller.produto_controller import ProdutoController

# Cria tabelas
Usuario.criar_tabela()
Produto.criar()

# Cadastro inicial de usuario
print("\n ==== CADASTRO DE USUÁRIO === ")

login = input("Novo usuário: ")
senha = input("Senha: ")

Usuario.cadastrar(login,senha)

# Login
print("\n === LOGIN ===")

login, senha = LoginView.exibir()

usuario = LoginController.autenticar(
    login,
    senha
)

if usuario:
    print("\n Login realizado \n")
    while True:
        opcao = ProdutoView.menu()
        if opcao == "1":
            ProdutoController.cadastrar()
        elif opcao == "2":
            produtos = Produto.consultar()
            print("zn === PRODUTOS === \n")
            for p in produtos:
                print(p)
        elif opcao == "3":
            id_produto = int(input("ID do produto para excluir: "))
            Produto.excluir(id_produto)
            print("Produto removido")
        elif opcao == "4":
            Produto.exportar()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida")
    else: print("Usuario ou senha incorretos.")
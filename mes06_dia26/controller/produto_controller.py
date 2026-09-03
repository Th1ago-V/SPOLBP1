from model.produto_model import Produto

class ProdutoController:
    @staticmethod
    def cadastrar():
        nome = input("Nome: ")
        modelo = input("Modelo: ")
        fabricante = input("Fabricante: ")
        preco = input("Preço: ")

        Produto.inserir(nome,modelo,fabricante,preco)

        print("Cadastrado com sucesso")

    @staticmethod
    def consultar():
        produtos = Produto.consultar()
        print("\n === LISTA DE PRODUTOS === \n")
        for produto in produtos:
            print(produto)

    @staticmethod
    def excluir():
        id_produto = input("ID do produto a excluir: ")
        Produto.excluir(id_produto)
        print("Produto excluido")
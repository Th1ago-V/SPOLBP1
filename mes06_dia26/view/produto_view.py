class ProdutoView:
    @staticmethod
    def menu():
        print("\n === MENU === \n")
        print("1 - Cadastrar")
        print("2 - Consultar")
        print("3 - Excluir")
        print("4 - Exportar")
        print("0 - Sair")
        return input("Escolha: ")
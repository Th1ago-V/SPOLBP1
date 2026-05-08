# controllers/supermercado_controller.py

from models.produto_model import Produto
from models.compra_model import ItemCompra
from views.supermercado_view import SupermercadoView

class SupermercadoController:
	#Construtor
	def __init__(self):
	# Lista de produtos cadastrador
		self.produtos = []
	# View
		self.view = SupermercadoView()
	def cadastrar_produto(self):
		nome, preco = self.view.obter_dados_produtos()
		produto = Produto(nome, preco)
		self.produtos.append(produto)
		print("Produto cadastrado com sucesso!")
# Listar produtos
	def listar_produto(self):
		if len(self.produtos) == 0:
			print("Nenhuma produto cadastrado.")
			return

		self.view.mostrar_produtos(self.produtos)

# Registrar  compra
	def registrar_compra(self):
		if len(self.produtos) == 0:
			print("Cadastre produtos primeiro.")
			return

		item_compra = []

		while True:
			#Mostrar produtos
			self.view.mostrar_produtos(self.produtos)
			codigo = self.view.escolher_produto()

			if codigo<0 or codigo>= len(self.produto):
				print("Código inválido.")
				continue

			quantidade = self.view.obter_quantidade()
			produto = self.produtos[codigo]
			item = ItemCompra(produto, quantidade)
			itens_compra.append(item)
			continuar = input("Adcionar mais itens? (s/n)")
			if continuar.lower() != "s":
				break

	# Executar sistema
	def executar(self):
		while True:
			opcao = self.view.menu()
			if opcao == "1":
				self.cadastrar_produto()
			elif opcao == "2":
				self.registrar_compra()
			elif opcao == "3":
				self.listar_produtos()
			elif opcao == "0":
				print("Sistema encerrado")
				break

			else:
				print("Opção inválido.")

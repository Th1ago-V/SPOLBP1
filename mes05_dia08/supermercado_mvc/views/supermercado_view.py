class SupermercadoView:
	# Exibir menu principal
	def menu(self):
		print("\n===== SUPERMERCADO MVC =====")
		print("1 - Cadastrar Produto")
		print("2 - Registrar Compra")
		print("3 - Listar Produtos")
		print("0 - Sair")

		return input("Escolha uma opção: ")

	#Entrada de produtos
	def obter_dados_produto(self):
		nome = input("Nome do produto: ")
		preco = float(input("Preço do produto: "))

	#Mostrar produtos
	def mostrar_produtos(self, produtos):
		print("\n===== PRODUTOS CADASTRADOS =====")
		for i, produto in enumerate(produtos):
			print(f"{i} - {produto.nome} | R$ {produto.preco:.2f}")

	#Escolher produto
	def escolher_produto(self):
		return int(input("Digite o código do produto: "))

	# Quantidade
	def obter_quantidade(self):
		return int(input("Quantidade: "))

	#Exibir fatura
	def mostrar_fatura(self, itens, total):
		print("\n===== FATURA =====")
		for item in itens:
			subtotal = items.subtotal()
			print(
				f"{item.produto.nome}"
				f"|Quantidade: {item.quantidade}"
				f"|Unitário: R${item.produto.preco:.2f}"
				f"|Subtotal: R${subtotal:.2f}"
			)
		print("\n TOTAL DA COMPRA: R${:.2f}".format(total))

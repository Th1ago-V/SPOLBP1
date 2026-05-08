# models/compra_model.py

class ItemCompra:
	#construtor
	def __init__(self, produto, quantidade):
		self.produto = produto
		self.quantidade = quantidade

	#Calculo subtotal
	def subtotal(self):
		return self.produto.preco * self.quantidade

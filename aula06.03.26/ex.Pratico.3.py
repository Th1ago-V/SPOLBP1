class Cereais:
  def __init__(self, nome, preço):
    self.nome = nome
    self.preço = preço

  def mostrar_preço(self,preço):
    print("O preço é",preço)

class Milho(Cereais):

  def mostrar_preço(self):
    print("O preço do",self.nome,"é",self.preço)

class Trigo(Cereais):

  def mostrar_preço(self):
    print("O preço do",self.nome,"é",self.preço)

class Aveia(Cereais):

  def mostrar_preço(self):
    print("O preço da",self.nome,"é",self.preço)

cereal1 = Milho("Milho", input("Entre com o preço do Milho: "))
cereal2 = Trigo("Trigo", input("Entre com o preço do Trigo: "))
cereal3 = Aveia("Aveia", input("Entre com o preço da Aveia: "))

cereal1.mostrar_preço()
cereal2.mostrar_preço()
cereal3.mostrar_preço()

class Carro:
  def __init__(self,cor,modelo):
    self.cor = cor
    self.modelo = modelo

  def acelerar(self):
    print("O carro está acelerando")

carro = Carro("Vermelho", "Fusca")
print(carro.modelo)
print(carro.cor)
carro.acelerar()

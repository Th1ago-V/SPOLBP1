class Jogador:
  def __init__(self,nome,pv,dano):
    self.nome = nome
    self.pv = pv
    self.dano = dano


print("----COMO JOGAR----") 
print("Para jogar, abra outras aba do navegador para jogar dados. Escolha sua classe, ela informa sua vida e seu dado de dano.")
print("----CLASSES----")
print("As classes são:")
print("1. GUERREIRO - 12 de vida - Dado de 4 faces")
print("2. LADINO - 10 de vida - Dado de 6 faces")
print("3. MAGO - 8 de vida - Dado de 8 faces")

cs = input("Entre com o número que corresponde a classe desejada: ")
if cs == 1:
  jdr = Jogador(input("Entre com seu nome:"), 12, "dado 4 faces")
else if cs == 2:
  jdr = Jogador(input("Entre com seu nome:"), 10, "dado 6 faces")
else if cs == 3:
  jdr = Jogador(input("Entre com seu nome:"), 8, "dado 8 faces")
else
   print("Escolha invalida")

class Monstro:
  def __init__(self,vida,dado):
    self.vida = vida
    self.dado = dado

monstro = Monstro(20, input("Entre com o resultado do dado de 6 faces: "))

class Jogador:
  def __init__(self,nome,pv,dano):
    self.nome = nome
    self.pv = pv
    self.dano = dano


print("----COMO JOGAR----") 
print("Para jogar, abra outras aba do navegador para jogar dados. Escolha sua classe, ela informa sua vida e seu dado de dano.")
print("Você vai enfrentar um monstro, os dados vão determinar o vencedor.")
print("----CLASSES----")
print("As classes são:")
print("1. GUERREIRO - 12 de vida - Dado de 4 faces")
print("2. LADINO - 10 de vida - Dado de 6 faces")
print("3. MAGO - 8 de vida - Dado de 8 faces")

i = 0
while i == 0:
  cs = int(input("Entre com o número que corresponde a classe desejada: "))
  if cs == 1:
    jdr = Jogador(input("Entre com seu nome: "), 12, "dado 4 faces")
    i = 1
  elif cs == 2:
    jdr = Jogador(input("Entre com seu nome: "), 10, "dado 6 faces")
    i = 1
  elif cs == 3:
    jdr = Jogador(input("Entre com seu nome: "), 8, "dado 8 faces")
    i = 1
  else:
    print("Escolha invalida")

class Monstro:
  def __init__(self,vida,dado):
    self.vida = vida
    self.dado = dado

monstro = Monstro(20, "dado de 6 faces: ")

print("\n ----COMBATE----")
print("Um monstro apareceu. Prepare-se ", jdr.nome)

j = 0
while j == 0:

  print("\n")
  print("Turno do ", jdr.nome, ". Role o ", jdr.dano)
  dmg = int(input("Entre com o valor rolado: "))
  print(jdr.nome," atacou o monstro atacou causando", dmg, " de dano")
  monstro.vida = monstro.vida - dmg
  if monstro.vida <= 0:
    print("\n O monstro foi derrotado")
    j = 1
    break

  print("\n")
  print("Turno do monstro. ")
  dmg2 = int(input("Entre com o resultado do dado de 6 faces: "))
  jdr.pv = jdr.pv - dmg2
  print("O monstro atacou ", jdr.nome, " causando", dmg2, " de dano")
  if jdr.pv <= 0:
    print("\n", jdr.nome, "foi derrotado(a)")
    j = 1
    break

  else:
    print("\n")
    print("> PROXIMA RODADA < ")

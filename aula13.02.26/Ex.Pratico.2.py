nome = input('Entre com seu nome: ')
print("Olá, ", nome)
n1 = int(input('Insira a primeira nota:'))
n2 = int(input('Insira a segunda nota:'))
m = (n1+n2)/2
if(m >= 6):
  print(nome, 'foi aprovado com média ', m)
else:
  print(nome, 'foi reprovado com média ', m)

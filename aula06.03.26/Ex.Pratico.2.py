## Sistema de Funcionáirios
class Funcionario:
  def calcular_bonus(self):
    print("Bonûs padrão")

## Gerente
class Gerente(Funcionario):
  def calcular_bonus(self):
    print("Bônus de 20% do salário")

## Estagiario
class Estagiario(Funcionario):
  def calcular_bonus(self):
    print("Bônus de 5% do salário")

f1 = Gerente()
f2 = Estagiario()

f1.calcular_bonus()
f2.calcular_bonus()

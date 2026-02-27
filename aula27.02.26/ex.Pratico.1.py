## CLASSE PAI
class Animal:
  def __init__(self, nome):
    self.nome = nome

  def emitir_som(self):
    print("Som genérico")

## CLASSE FILHA
class Cachorro(Animal):
  def emitir_som(self):
    print("Meu cachorro",self.nome,"faz")
    print("Au au")

## CLASSE FILHA
class Gato(Animal):
  def emitir_som(self):
    print("Meu gato",self.nome,"faz")
    print("Miau")

dog = Cachorro("Rex")
dog.emitir_som()

cat = Gato("Ploc")
cat.emitir_som()
    

class FORMA:
  def area(self):
    print("Calculando área...")

class QUADRADO(FORMA):
  def __init__(self,lado):
    self.lado = lado

  def area(self):
    resultado = self.lado * self.lado
    print("Área do quadrado:",resultado)

import math

class CIRCULO(FORMA):
  def __init__(self,raio):
    self.raio = raio

  def area(self):
    resultado = math.pi * self.raio ** 2
    print("Área do círculo:",resultado)

q = QUADRADO(4)
c = CIRCULO(3)

q.area()
c.area()

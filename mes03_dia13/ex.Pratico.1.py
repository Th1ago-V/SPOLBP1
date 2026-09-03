import math

class Pessoa:
  def __init__(self, nome):
    self.nome = nome

class Aluno(Pessoa):
  def __init__(self,nome, prontuario):
    self.nome = nome
    self.prontuario = prontuario

class Disciplina:
  def __init__(self, dnome, dprof, dnum, dnota, dtrab, dmedia, dsitu):
    self.dnome = dnome
    self.dprof = dprof
    self.dnum = dnum
    self.dnota = dnota
    self.dtrab = dtrab
    self.dmedia = dmedia
    self.dsitu = dsitu

class DisciplinaReg(Disciplina):
    def CalcMed(self):
      self.dmedia = (self.dnota + self.dtrab)/2
      self.dmedia = math.ceil(self.dmedia)
      if self.dmedia >= 7.0:
        print("Aprovado com média", f"{self.dmedia:.2f}", "\n") 
      elif 5 < self.dmedia < 6.9 :
        print("Recuperação. com média", f"{self.dmedia:.2f}", "\n")
      else:
        print("Reprovado com média", f"{self.dmedia:.2f}", "\n")

print("=======================")
print("RELATÓRIO DO ALUNO")
print("=======================")

aluno = Aluno(input("Entre com o nome do aluno: "),input("Entre com o prontuário do aluno: "))

disp = [] 

print("\n")
for i in range(4):
  disciplina = DisciplinaReg(input("Entre com a disciplina: "),
      input("Entre com o professor: "),
      float(input("Entre com o número de aulas: ")), 
      int(input("Entre com a nota da prova: ")),
      int(input("Entre com a nota do trabalho: ")),
      0.0, 
      "neutra")
  
  disciplina.CalcMed()

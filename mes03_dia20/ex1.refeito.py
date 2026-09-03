## Código finalizado, erros corrigidos

class Aluno():
	def __init__(self, Nome, NotaTB1, NotaTB2, NotaP, NotaF):
		self.Nome =  Nome
		self.NotaTB1 =  NotaTB1
		self.NotaTB2	=  NotaTB2
		self.NotaP =  NotaP
		self.NotaF =  NotaF

	def CalcMed(self):
		self.NotaF = ((self.NotaTB1 + self.NotaTB2)/2)*0.3 + (self.NotaP)*0.7 
		print("Média Final: ", alunos.NotaF, "\n")

alunos = [4]

for i in range(4):
	print("CADASTRO DO ALUNO ", i+1)
	alunos = Aluno(input("Entre com o nome do aluno: "), 
                   float(input("Entre com a nota do trabalho 1: ")), 
                   float(input("Entre com a nota do trabalho 2: ")), 
                   float(input("Entre com a nota da prova: ")),
                   0.0)
	
	print("\n")

	print("RELATÓRIO DO ALUNO ", i+1)
	print("Aluno: ", alunos.Nome)
	print("Nota do Trabalho 1: ", alunos.NotaTB1)
	print("Nota do Trabalho 2: ", alunos.NotaTB2)
	print("Nota da Prova: ", alunos.NotaP)
	alunos.CalcMed() 

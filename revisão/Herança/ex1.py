class Funcionario:
     def __init__(self, nome, cpf, sal):
          self.nome = nome
          self.cpf = cpf
          self.salario = sal

     def aumentarSalario(self, aumento):
          self.salario = self.salario + aumento

class Desenvolvedor(Funcionario):
     def __init__(self, nome, cpf, sal, ling):
          super().__init__(nome, cpf, sal)
          self.linguagem = ling

     def trocarLinguagem(self, novaLing):
          self.linguagem = novaLing

     def __str__(self):
          return f"Nome:{self.nome} | CPF:{self.cpf} | Salario:{self.salario} | Linguagem:{self.linguagem}"      

desen=Desenvolvedor("Tulio",98675,1500,"JAVA")
print(desen)
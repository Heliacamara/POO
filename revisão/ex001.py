#Declaração de classe
class Gafanhoto:
    def __init__(self): #Método Construtor
      #Atributos de instância
      self.nome = ""
      self.idade = 0
      self.bolsa= 0

    #Métodos de instância
    def aniversario(self):
       self.idade = self.idade + 1

    def bolsas(self):
       self.bolsa= self.bolsa + 1

    def mensagen(self):
       return   f"{self.nome} e Gafanhoto(a) e tem {self.idade} anos de idade, possui {self.bolsa} bolsas!"




#Declaração de objeto
g1= Gafanhoto()
g1.nome= 'Maria'
g1.idade = 17
g1.bolsa= 2
g1.aniversario()
g1.bolsas()
print(g1.mensagen())

g2= Gafanhoto()
g2.nome= 'Mauro'
g2.idade= 53
g2.bolsa= 3
g2.aniversario()
g2.bolsas()
print(g2.mensagen())

g3= Gafanhoto()
g3.nome= 'Helia'
g3.idade= 16
g3.bolsa= 4
g3.aniversario()
g3.bolsas()
print(g3.mensagen())
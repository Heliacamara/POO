class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade= idade

    def apresentar(self,):
        print(f"Meu nome e {self.nome}; e tenho {self.idade}")    

p1= Pessoa("Ana",20)
p1.apresentar()        
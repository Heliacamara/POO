class Funcionario:
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario

    def exibir_dados(self):
        return f"Nome:{self.nome}; Salario{self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, salario,bonus):
        super().__init__(nome, salario)
        self.bonus=bonus

    def exibir_dados(self):
        return f"Nome:{self.nome}; Salario:{self.salario}; Bonus:{self.bonus}"    

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario,linguagem):
        super().__init__(nome, salario)
        self.linguagem=linguagem

    def exibir_dados(self):
        return f"Nome:{self.nome}; Salario:{self.salario}; Linguagem:{self.linguagem}"

gege=Gerente("Vitor",4000,200)
print(gege.exibir_dados())

desen=Desenvolvedor("Helia",4000,"C++")
print(desen.exibir_dados())
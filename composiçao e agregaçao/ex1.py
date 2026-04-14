class Cidade:
    def __init__(self,nome):
        self.__nome:str= nome
    @property
    def nome(self):
        return self.nome
    def __str__(self):
        return f"Cidade: {self.__nome}"

class Pessoa:
    def __init__(self,nome,cidade):
        self.nome:str=nome
        self.cidade=cidade
    def __str__(self):
        return f"Cidade:{self.cidade}, Nome:{self.nome}"

class Animal:
    def __init__(self,nome,pessoa):
        self.nome:str=nome 
        self.dono=pessoa

    def __str__(self):
        return f"Nome:{self.nome},dono:{self.dono.nome}"

municipio=Cidade("Santa-Maria")
people=Pessoa("Hélia",municipio)
dog= Animal("babosta",people)

print(municipio)
print(people)
print(dog)

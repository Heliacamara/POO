class Cidade:
    def __init__(self,nome):
        self.__nome:str=nome

class Pessoa:
    def __init__(self,nome):
        self.nome:str=nome
        self.cidade=Cidade()

class Animal:
    def __init__(self,nome):
        self.nome:str=nome
        self.dono=Pessoa()
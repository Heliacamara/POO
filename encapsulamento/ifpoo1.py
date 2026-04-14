class Estudante:
    def __init__(self,id,nome):
        self.nome=nome
        self.__id= id 
        self.__creditos= 1

    @property
    def id(self):
        return self.__id

    @property
    def creditos(self):
        return self.__creditos    
    
    @creditos.setter
    def creditos(self,valor):
        if valor > 0:
            self.__creditos= valor
        else:
            self.__creditos= 1    

    def detalhar(self):
        print(f'Nome:{self.nome}')
        print(f'Id:{self.__id}')
        print(f'Creditos:{self.__creditos}')


estu1= Estudante(1,"Ana")
estu2= Estudante(2,"Vitor")

estu1.creditos= 5
estu2.creditos= 8

estu1.detalhar()
estu2.detalhar()

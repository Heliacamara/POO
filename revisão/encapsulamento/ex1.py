class Estudante:
    def __init__(self,id,nome,creditos):
       self.__id= id
       self.nome=nome
       self.__creditos=1
       self.creditos=creditos

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self,valor):
        if valor >0:
            self.__creditos=valor
        else:
            self.__creditos=1    

    def detalhar(self):
        print(f"O ID:{self.__id},nome:{self.nome},creditos:{self.__creditos}")


p1=Estudante(100,"Bruna",-24)
p2=Estudante(800,"Camila",99)
p1.detalhar()
p2.detalhar()
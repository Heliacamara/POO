class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn:int=isbn

    def exibir_detalhes(self):
        print(f"Titulo do livro: {self.titulo}") 
        print(f"Autor do livro: {self.autor}")
        print(f"O numero de identificacao do livro(ISBN): {self.isbn}")

class Membro:
    def __init__(self,nome,id_membro,contato):
        self.nome=nome
        self.__id_membro=id_membro
        self.contato=contato

    @property
    def id_membro(self):
        return self.__id_membro

    @id_membro.setter
    def id_membro(self,idmembro):
        if idmembro<0:
            print("Nao pode ser atribuido ao id valores negativos")
        else:
            self.__id_membro=idmembro

    def __str__(self):
        return (f"Quem pegou o livro: {self.nome} |Id_membro: {self.id_membro}")
        

    def exibir_detalhes(self):
        print(f"Quem pegou o livro: {self.nome}") 
        print(f"Id_membro: {self.id_membro}")
        print(f"Contato de quem pegou o livro: {self.contato}")

p1=Membro("Helia",10,"helia@gmail.com")
print(p1)
p1.id_membro=-5
print(p1)
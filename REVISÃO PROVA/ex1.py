class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn:int=isbn

    def exibir_detalhes(self):
        print(f"Titulo do livro: {self.titulo}") 
        print(f"Autor do livro: {self.autor}")
        print(f"O numero de indentificacao do livro(ISBN): {self.isbn}")

class Membro:
    def __init__(self,nome,id_membro,contato):
        self.nome=nome
        self.id_membro=id_membro
        self.contato=contato

    def exibir_detalhes(self):
        print(f"Quem pegou o livro: {self.nome}") 
        print(f"Id_membro: {self.id_membro}")
        print(f"Contato de quem pegou o livro: {self.contato}")

l1=Livro("O misterio do verde nasce","Ana Claudia Trigueiro",34)
l1.exibir_detalhes()
p1=Membro("Hélia",12345,"camarahehe@gmail.com")
p1.exibir_detalhes()
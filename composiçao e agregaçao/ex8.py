class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
    def __str__(self):
        return f"{self.titulo}, autor: {self.autor}."

class Biblioteca:
    def __init__(self,nome):
        self.nome=nome
        self.lista_de_livros=[]

    def adicionar_livros(self, livro):
        self.lista_de_livros.append(livro)

    def listar_livros(self):
        for livro in self.lista_de_livros:
            print(f"A biblioteca {self.nome}  tem o livro {livro}")   

l1=Livro("O ursinho","Helia")
l2=Livro("A borboletinha na cozinha","Vitinho")
bibli=Biblioteca("Chica doida") 
bibli.adicionar_livros(l1)
bibli.adicionar_livros(l2)
bibli.listar_livros()

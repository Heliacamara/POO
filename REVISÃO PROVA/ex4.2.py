class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn:int=isbn

    def exibir_detalhes(self):
        print(f"Titulo do livro: {self.titulo}") 
        print(f"Autor do livro: {self.autor}")
        print(f"O numero de identificacao do livro(ISBN): {self.isbn}")

class LivroDigital(Livro):
    def __init__(self, titulo, autor, isbn,formato,tamanho_mb):
        super().__init__(titulo, autor, isbn)
        self.formato=formato
        self.tamanho_mb:float=tamanho_mb

    def exibir_detalhes(self):
        print("-------------")
        print(f"Titulo do livro: {self.titulo}") 
        print(f"Autor do livro: {self.autor}")
        print(f"O numero de identificacao do livro(ISBN): {self.isbn}")
        print(f"O formato do arquivo{self.formato}")
        print(f"O tamanho do arquivo:{self.tamanho_mb} MB")

ob1=Livro("Joao pe de feijao","Helia",10)
ob1.exibir_detalhes() #Nao usei print pq no metodo ja tem
ob2=LivroDigital("Joao pe de feijao","Helia",10,"PDF",60)
ob2.exibir_detalhes()

# Demonstração do polimorfismo

lista_livros = [ob1, ob2]

for livro in lista_livros:
    livro.exibir_detalhes()
                
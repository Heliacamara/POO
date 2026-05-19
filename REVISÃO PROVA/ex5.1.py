from abc import ABC,abstractmethod

class ItemBiblioteca(ABC):
    @abstractmethod
    def get_identificador(self):
        pass

class Livro(ItemBiblioteca):
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn:int=isbn

    def exibir_detalhes(self):
        print(f"Titulo do livro: {self.titulo}") 
        print(f"Autor do livro: {self.autor}")
        print(f"O numero de identificacao do livro(ISBN): {self.isbn}")

    def get_identificador(self):
        return self.isbn


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
        print(f"O formato do arquivo:{self.formato}")
        print(f"O tamanho do arquivo:{self.tamanho_mb} MB")

ob2=LivroDigital("Joao pe de feijao","Helia",10,"PDF",60)
ob2.exibir_detalhes()

print(f"Identificador:{ob2.get_identificador()}")
        
#A classe abstrata garante que todo item da biblioteca tenha um identificador, independentemente do tipo (livro físico, digital, revista etc.), tornando o sistema mais seguro e organizado.
# vantagem de usar uma classe abstrata nesse contexto é que ela funciona como um contrato obrigatório.
#Isso significa que qualquer classe que herdar de ItemBiblioteca é obrigada a implementar o método.                   
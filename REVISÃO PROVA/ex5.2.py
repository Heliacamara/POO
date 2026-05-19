from abc import ABC, abstractmethod
# Importa ferramentas para criar classe abstrata

class ItemBiblioteca(ABC):
    # Classe abstrata que serve como modelo

    @abstractmethod
    def get_identificador(self):
        # Método obrigatório para todas as subclasses
        pass


class LivroNaoEncontradoError(Exception):
    # Exceção personalizada para quando o livro não for encontrado
    pass


class Livro(ItemBiblioteca):
    # Classe Livro herda de ItemBiblioteca

    def __init__(self, titulo, autor, isbn):
        # Construtor da classe Livro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn  # Identificador único do livro

    def exibir_detalhes(self):
        # Mostra informações do livro
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")

    def get_identificador(self):
        # Implementação obrigatória da classe abstrata
        return self.isbn


class LivroDigital(Livro):
    # LivroDigital herda de Livro

    def __init__(self, titulo, autor, isbn, formato, tamanho_mb):
        # Chama o construtor da classe pai (Livro)
        super().__init__(titulo, autor, isbn)

        self.formato = formato
        self.tamanho_mb = tamanho_mb

    def exibir_detalhes(self):
        # Sobrescreve o método da classe Livro (polimorfismo)
        print("-------------")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Formato: {self.formato}")
        print(f"Tamanho: {self.tamanho_mb} MB")


class Biblioteca:
    # Classe que gerencia os livros

    def __init__(self):
        # Lista onde os livros serão armazenados
        self.catalogo_livros = []

    def adicionar_livro(self, livro):
        # Adiciona um livro ao catálogo
        self.catalogo_livros.append(livro)

    def buscar_livro_por_isbn(self, isbn):
        # Percorre todos os livros da biblioteca

        for livro in self.catalogo_livros:
            # Verifica se o ISBN bate com o buscado
            if livro.get_identificador() == isbn:
                return livro  # Retorna o livro encontrado

        # Se não encontrar nenhum livro, lança erro personalizado
        raise LivroNaoEncontradoError(
            f"Livro com ISBN {isbn} nao encontrado."
        )


# ---------------- TESTE DO SISTEMA ----------------

livro1 = Livro("Dom Casmurro", "Machado de Assis", 100)
# Criação de um livro normal

livro2 = LivroDigital("Python", "Helia", 200, "PDF", 50)
# Criação de um livro digital

bib = Biblioteca()
# Criação da biblioteca

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
# Adicionando livros ao catálogo

try:
    # Tentativa de buscar um livro pelo ISBN
    livro_encontrado = bib.buscar_livro_por_isbn(200)

    print("Livro encontrado:")
    livro_encontrado.exibir_detalhes()

except LivroNaoEncontradoError as erro:
    # Caso não encontre o livro, mostra a mensagem de erro
    print(erro)
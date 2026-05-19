class Biblioteca:
    def __init__(self,nome):
        self.nome=nome
        self.catalogo_livros=[]
        self.lista_membros=[]

    def adicionar_livro(self,livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self,membro):
        self.lista_membros.append(membro)

    def buscar_livro_por_isbn(self,isbn):
        pass    
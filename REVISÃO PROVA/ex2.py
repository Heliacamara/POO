class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn

class Membro:
    def __init__(self,nome,id_membro,contato):
        self.nome=nome
        self.id_membro=id_membro
        self.contato=contato

class Biblioteca:
    def __init__(self,nome):
        self.nome=nome
        self.catalogo_livros=[]
        self.lista_membros=[]

    def adicionar_livro(self,livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self,membro):
        self.lista_membros.append(membro)

class Emprestimo:
    def __init__(self,data_emprestimo,data_devolucao,livro,membro):
        self.livro=livro
        self.membro=membro
        self.data_emprestimo=data_emprestimo
        self.data_devolucao=data_devolucao

livro1=Livro("Python","Carlos","123")
membro1=Membro("Helia",1,"helia@gmail.com")

biblioteca1=Biblioteca("Biblioteca Central")
biblioteca1.adicionar_livro(livro1)
biblioteca1.adicionar_membro(membro1)

emprestimo1=Emprestimo("10/05/2026","20/05/2026",livro1,membro1)
print(biblioteca1.nome)
print(biblioteca1.catalogo_livros[0].titulo)
print(biblioteca1.lista_membros[0].nome)
print(emprestimo1.data_emprestimo)
print(emprestimo1.livro.titulo)
print(emprestimo1.membro.nome)

# Cria um objeto da classe Livro
#livro1=Livro("Python","Carlos","123")

# Cria um objeto da classe Membro
#membro1=Membro("Helia",1,"helia@gmail.com")

# Cria uma biblioteca
#biblioteca1=Biblioteca("Biblioteca Central")

# Adiciona o livro na lista de livros da biblioteca
#biblioteca1.adicionar_livro(livro1)

# Adiciona o membro na lista de membros da biblioteca
#biblioteca1.adicionar_membro(membro1)

# Cria um empréstimo relacionando livro e membro
#emprestimo1=Emprestimo("10/05/2026","20/05/2026",livro1,membro1)

# Mostra o nome da biblioteca
#print(biblioteca1.nome)

# Mostra o título do primeiro livro cadastrado
#print(biblioteca1.catalogo_livros[0].titulo)

# Mostra o nome do primeiro membro cadastrado
#print(biblioteca1.lista_membros[0].nome)

# Mostra a data do empréstimo
#print(emprestimo1.data_emprestimo)

# Mostra o título do livro emprestado
#print(emprestimo1.livro.titulo)

# Mostra o nome do membro que pegou o livro
#print(emprestimo1.membro.nome)


## É um exemplo de agregação porque a classe Emprestimo
# utiliza objetos das classes Livro e Membro,
# mas eles continuam existindo independentemente do empréstimo.
# Mesmo que o empréstimo seja removido,
# os objetos Livro e Membro continuam existindo.
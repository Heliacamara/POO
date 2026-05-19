class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn = isbn

    def exibir_detalhes(self):
        return f"Titulo do livro: {self.titulo} | Autor: {self.autor} | ISBN: {self.isbn}"


class Membro:
    def __init__(self,nome,id_membro,contato):
        self.nome=nome
        self.id_membro=id_membro
        self.contato=contato


# O método __init__ é o construtor da classe.
# Ele é executado automaticamente quando um objeto é criado.

# O parâmetro self representa o próprio objeto,
# permitindo acessar atributos e métodos da classe.


l1=Livro("O misterio do verde nasce","Ana Claudia Trigueiro",34)
print(l1.exibir_detalhes())

p1=Membro("Hélia",12345,"camarahehe@gmail.com")
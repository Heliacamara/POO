class Autor:
    def __init__(self,autor):
        self.autor:str=autor

class Livro:
    def __init__(self,livro,autor):
        self.livro=livro
        self.autor= Autor(autor)
    def __str__(self):
        return f"O nome do livro: {self.livro} e seu autor:  {self.autor.autor}"
livro= Livro("O bananao","Vitini")
print(livro)
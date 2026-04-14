class Professor:
    def __init__(self,nome,titulacao):
        self.nome=nome
        self.titulacao=titulacao

class Disciplina:
    def __init__(self,nome,professor):
        self.nome=nome
        self.professor=professor

    def mostrar(self):
        print(f"A(o) professora(o) {self.professor} tem a disciplina {self.nome}.")

p1=Professor("Léo","Doutor")
p2=Professor("Joyce","Doutora")
d1=Disciplina("IP",p1.nome)
d2=Disciplina("Sociologia",p2.nome)
d1.mostrar()
d2.mostrar()

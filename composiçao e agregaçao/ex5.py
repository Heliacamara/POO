class Professor:
    def __init__(self,nome,titulacao):
        self.nome=nome
        self.titulacao=titulacao

class Disciplina:
    def __init__(self,nome,professor):
        self.nome=nome
        self.professor=professor

    def mostrar(self):
        print(f"A(o) professora(o) {self.professor.nome} tem a disciplina {self.nome}")
        print(f"Titulacao: {self.professor.titulacao}")

p1 = Professor("Leo", "Doutor")
p2 = Professor("Joyce", "Doutora")
d1 = Disciplina("IP",p1)
d2 = Disciplina("Sociologia",p2)
d1.mostrar()
d2.mostrar()

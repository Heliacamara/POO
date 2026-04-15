class Aluno:
    def __init__(self,aluno):
        self.aluno = aluno

    def __str__(self):
        return f"Nome do aluno(a): {self.aluno}"
    
class Turma:
    def __init__(self,nome):
        self.nome = nome
        self.lista_alunos=[]

    def __str__(self):
        return f"Nome da turma: {self.nome}"
    
    def adicionar_aluno(self, aluno):
        self.lista_alunos.append(aluno)

    def exibir_turma(self):
        for aluno in self.lista_alunos:
            print(f"{aluno}, turma: {self.nome}")

class Escola:
    def __init__(self, nome):
        self.nome = nome 
        self.lista_turma=[]

    def adicionar_turma(self, turma):
        self.lista_turma.append(turma)

    def exibir_turmas(self):
        print(f"Escola {self.nome}:")
        for turma in self.lista_turma:
            turma.exibir_turma()

escola = Escola("SELM")
aluno1 = Aluno("Hélia")
turma = Turma("Os batatinhas")
turma.adicionar_aluno(aluno1)
escola.adicionar_turma(turma)
escola.exibir_turmas()
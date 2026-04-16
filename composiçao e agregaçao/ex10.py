class Aluno:
    def __init__(self,aluno):
        self.aluno=aluno

    def __str__(self):
        return f"Nome do aluno(a): {self.aluno}"

class Turma:
    def __init__(self,nome):
        self.nome=nome
        self.lista_alunos=[]

    def __str__(self):
        return f"Nome da turma: {self.nome}"

    def adicionar_aluno(self, aluno):
        self.lista_alunos.append(aluno)

    def exibir_turma(self):
        print(f"Turma: {self.nome}")
        for aluno in self.lista_alunos:
            print(aluno)

class Escola:
    def __init__(self,nome):
        self.nome=nome
        self.lista_turma=[]

    def adicionar_turma(self,nome_turma):
        turma=Turma(nome_turma)
        self.lista_turma.append(turma)
        return turma

    def exibir_turmas(self):
        print(f"Escola {self.nome}:")
        for turma in self.lista_turma:
            turma.exibir_turma()
            print()

escola=Escola("SELM")
aluno1=Aluno("Helia")
aluno2=Aluno("Pedro")
turma1=escola.adicionar_turma("9ano A")
turma2=escola.adicionar_turma("8 ano C")
turma1.adicionar_aluno(aluno1)
turma2.adicionar_aluno(aluno2)
escola.exibir_turmas()
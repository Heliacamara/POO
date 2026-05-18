class Aluno:
    def __init__(self,aluno):
        self.aluno=aluno

    def __str__(self):
        return f"Nome do aluno:{self.aluno}"

class Turma:
    def __init__(self,nome):
        self.nome=nome
        self.lista_alunos=[]

    def __str__(self):
        return f"Nome da turma:{self.nome}"
        
    def adicionar_alunos(self,aluno):
        self.lista_alunos.append(aluno)

    def mostrar_turma(self):
        print(f"Turma:{self.nome}")
        for aluno in self.lista_alunos:
            print(aluno)


class Escola:
    def __init__(self,nome):
        self.nome=nome
        self.lista_turma=[]

    def adicionar_turmas(self,nome_turma):
        turma=Turma(nome_turma)
        self.lista_turma.append(turma)
        return turma
    
    def mostrar_turma(self):
        print(f"ESCOLA:{self.nome}")
        for turma in self.lista_turma:
            turma.mostrar_turma()
            print()
   
escola=Escola("SELM")
aluno1=Aluno("Helia")
aluno2=Aluno("Vitinho")
aluno3=Aluno("Gio")
aluno4=Aluno("Anny")
turma1=escola.adicionar_turmas("9 ano C")
turma2=escola.adicionar_turmas("6 ano A")
turma1.adicionar_alunos(aluno1)
turma1.adicionar_alunos(aluno2)
turma2.adicionar_alunos(aluno3)
turma2.adicionar_alunos(aluno4)
escola.mostrar_turma()
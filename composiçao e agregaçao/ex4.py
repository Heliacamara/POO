class Jogador:
    def __init__(self,nome,posicao):
        self.nome=nome
        self.posicao=posicao

class Time:
    def __init__(self,nome):
        self.nome=nome       
        self.lista_de_jogadores=[]

    def adicionar(self,jogador):
        self.lista_de_jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Os jogadores do {self.nome}:") 
        for jogador in self.lista_de_jogadores:
            print(f"{jogador.nome} ; Posicao:{jogador.posicao}")

p1=Jogador("Vitinho","goleiro")
p2=Jogador("Joabini","central")
p3=Jogador("Priminho","atacante")
time=Time("America")
time.adicionar(p1)
time.adicionar(p2)
time.adicionar(p3)
time.listar_jogadores()
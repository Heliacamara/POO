class Processador:
    def __init__(self,modelo,velocidade):
        self.modelo=modelo
        self.velocidade:float=velocidade

class Memoria:
    def __init__(self,capacidade):
        self.capacidade=capacidade

class Computador:
    def __init__(self,modelo,velocidade,capacidade):
        self.processador=Processador(modelo,velocidade)
        self.memoria=Memoria(capacidade)


    def exibir_configuracao(self):
        print(f"O modelo {self.processador.modelo} tem a velocidade {self.processador.velocidade} tem a memoria {self.memoria.capacidade} RAM")
        
obj1=Computador("Ryzen 7",4.7,16)
obj1.exibir_configuracao()
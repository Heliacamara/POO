class Motor:
    def __init__(self,potencia):
        self.potencia:int=potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligados.")

class Carro:
    def __init__(self,modelo,potencia):
        self.modelo:str=modelo
        self.motor = Motor(potencia)

    def ligar_carro(self):
        print(f"Ligando o {self.modelo}...") 
        self.motor.ligar()
carro=Carro("Corolla",200)    
carro.ligar_carro()               
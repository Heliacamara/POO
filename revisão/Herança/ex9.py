class Motor:
    def __init__(self,potencia):
        self.potencia=potencia

    def ligar_motor(self):
        print("O motor esta ligando")

    def exibir_info(self):
        print("O motor esta ligando")

class Eletrico:
    def __init__(self,bateria):
        self.bateria=bateria

    def carregar(self):
        pass

    def exibir_info(self):
        print("O carro esta carregando")   

class Combustao:
    def __init__(self,tanque):
        self.tanque=tanque  

    def abastecer(self):
        pass

    def exibir_info(self):
        print("O motor precisa abastecer")

class CarroEletrico(Motor,Eletrico):
    def __init__(self, potencia):
        super().__init__(potencia) 

class CarroHibrido(Motor,Eletrico,Combustao):
    def __init__(self, potencia):
        super().__init__(potencia)                     
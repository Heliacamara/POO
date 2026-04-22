class Motor:
    def __init__(self,potencia):
        self.potencia=potencia

    def ligar_motor(self):
        print("Ligando motor")

    def exibir_info(self):
        print(f"O motor tem de potencia:{self.potencia} cavalos")   

class Eletrico:
    def __init__(self,bateria):
        self.bateria=bateria

    def carregar(self):
        print("O carro esta carregando")

    def exibir_info(self):
        print(f"Esta carregando com uma bateria de: {self.bateria}kwh")    

class Combustao:
    def __init__(self,tanque):
        self.tanque=tanque

    def abastecer(self):
        print("O carro vai abastecer")

    def exibir_info(self):
        print(f"O carro vai abastecer para alcancar a sua quantidade maxima do tanque de {self.tanque}")                                    
        
class CarroEletrico(Motor,Eletrico):
    def __init__(self, potencia):
        super().__init__(potencia)

    def exibir_info(self):
        Motor.exibir_info()
        Eletrico.exibir_info()    

class CarroHibrido(Motor,Eletrico,Combustao):
    def __init__(self, potencia):
        super().__init__(potencia)

    def exibir_info(self):
        Motor.exibir_info()
        Eletrico.exibir_info()
        Combustao.exibir_info()                    
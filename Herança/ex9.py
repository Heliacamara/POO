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
        print(f"O carro vai abastecer para alcancar a sua quantidade maxima do tanque de {self.tanque} litros ")

class CarroEletrico(Motor,Eletrico):
    def __init__(self,potencia,bateria):  
        super().__init__(potencia)
        Eletrico.__init__(self,bateria) 

    def exibir_info(self):
        Motor.exibir_info(self)   
        Eletrico.exibir_info(self)

class CarroHibrido(Motor,Eletrico,Combustao):
    def __init__(self,potencia,bateria,tanque):
        super().__init__(potencia)
        Eletrico.__init__(self,bateria)
        Combustao.__init__(self,tanque)

    def exibir_info(self):
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)

print("INFORMACOES SOBRE O CARRO HIBRIDO:")
carrinho_hibribri=CarroHibrido(150,80,70)
carrinho_hibribri.exibir_info()

print("INFORMACOES SOBRE O CARRO ELETRICO:")
carrinho_eletritri=CarroEletrico(140,99)
carrinho_eletritri.exibir_info()
class Motor:
    def __init__(self,potencia):
        self.potencia=potencia

    def ligar_motor(self):
        print("Ligando motor")

    def exibir_info(self):
        print(f"O motor tem potencia de: {self.potencia} cavalos")

class Eletrico:
    def __init__(self,bateria):
        self.bateria=bateria

    def carregar(self):
        print("O carro esta carregando")

    def exibir_info(self):
        print(f"Bateria de: {self.bateria} kWh")

class Combustao:
    def __init__(self,tanque):
        self.tanque=tanque

    def abastecer(self):
        print("O carro vai abastecer")

    def exibir_info(self):
        print(f"Tanque de: {self.tanque} litros")

class Motor:
    def __init__(self, potencia, **kwargs):
        super().__init__(**kwargs)
        self.potencia = potencia

    def ligar_motor(self):
        print("Ligando motor")

    def exibir_info(self):
        print(f"Potência: {self.potencia}")

class Eletrico:
    def __init__(self, bateria, **kwargs):
        super().__init__(**kwargs)
        self.bateria = bateria

    def carregar(self):
        print("Carregando bateria")

    def exibir_info(self):
        print(f"Bateria: {self.bateria} kWh")

class Combustao:
    def __init__(self, tanque, **kwargs):
        super().__init__(**kwargs)
        self.tanque = tanque

    def abastecer(self):
        print("Abastecendo tanque")

    def exibir_info(self):
        print(f"Tanque: {self.tanque} Litros")

class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        super().__init__(potencia=potencia, bateria=bateria)

    def exibir_info(self):
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)

class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        super().__init__(potencia=potencia, bateria=bateria, tanque=tanque)

    def exibir_info(self):
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)


# Teste
c1 = CarroEletrico(150, 80)
c2 = CarroHibrido(200, 60, 50)

c1.exibir_info()
c2.exibir_info()
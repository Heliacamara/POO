class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo= modelo
        self.ano= ano

    def exibir_dados(self):
        print(f"A marca do carro: {self.marca}")
        print(f"O modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

c1=Carro("Fiat","Kiwid",2020)
c1.exibir_dados()            
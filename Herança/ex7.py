class Veiculo:
    def acelerar(self):
        print(f"Esta acelerando")

class Carro(Veiculo):
    def acelerar(self):
        print(f"Rafinha dirigiu um carro ontem.")

class Moto(Veiculo):
    def acelerar(self):
        print(f"Rafinha nao gosta de moto")

veiculuzinho=Veiculo()
veiculuzinho.acelerar()

carrinho=Carro()
carrinho.acelerar()

motinha=Moto()
motinha.acelerar()
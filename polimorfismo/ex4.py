class Veiculo:
    def mover(self):
        return "Veiculo se movendo"
    
class Carro(Veiculo):
    def mover(self):
        return "Carro andando"
    
class Moto(Veiculo):
    def mover(self):
        return "Moto se locomovendo"
    
class Bicicleta(Veiculo):
    def mover(self):
        return "Bicicleta se movendo"


veiculos= [Carro(),Moto(),Bicicleta()]

for diversos in veiculos:
    print(diversos.mover())
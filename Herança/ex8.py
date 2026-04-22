class Motor:
    def __init__(self,nome_motor):
        self.nome_motor=nome_motor

    def tipo(self): 
        return "Motor a gas"

class Carro:
    def __init__(self,nome_motor):
        self.nome_motor=Motor(nome_motor)

    def mostrar(self):
        return f"Motor: {self.nome_motor.nome_motor} ({self.nome_motor.tipo()})"

class MotorEletrico(Motor):
    def __init__(self,nome_motor,energia):
        super().__init__(nome_motor)
        self.energia=energia

    def tipo(self):
        return "Motor eletrico"

class CarroEletrico(Carro):
    def __init__(self,nome_motor,energia):
        super().__init__(nome_motor)
        self.nome_motor=MotorEletrico(nome_motor,energia)

    def mostrar(self):
        return f"Motor: {self.nome_motor.nome_motor} ({self.nome_motor.tipo()});Energia: {self.nome_motor.energia}"

carrinho=Carro("2.5")
carrao=CarroEletrico("hibrido", 200)

print(carrinho.mostrar())
print(carrao.mostrar())
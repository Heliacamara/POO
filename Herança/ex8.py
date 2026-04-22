class Motor:
    def __init__(self,nome_motor):
        self.nome_motor=nome_motor

class Carro:
    def __init__(self,nome_motor):
        self.nome_motor=Motor(nome_motor)
         
class MotorEletrico(Motor):
    def __init__(self,energia):
        self.energia=energia

class CarroEletrico(Carro):
    def __init__(self, nome_motor,energia):
        super().__init__(nome_motor)
        self.nome_motor=MotorEletrico(energia) 



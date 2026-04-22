class Nadador:
    def mover(self):
         print(f"Vitor esta nadando, ganhando E lacrando.")

class Corredor:
    def mover(self):
        print(f"Vitinho esta batendo o seu PR.")

class Triatleta(Nadador,Corredor):
    def mover(self):
           Nadador.mover(self)
           Corredor.mover(self)

obb=Triatleta()
obb.mover()            
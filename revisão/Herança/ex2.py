class Computador:
    def __init__(self,processador,memoria):
        self.processador:str = processador
        self.memoria:float = memoria

    def __str__(self):
        return f"COMPUTADOR / PROCESSADOR:{self.processador} / MEMORIA:{self.memoria}"


class Laptop(Computador):
    def __init__(self, processador, memoria, bateria=0):
        super().__init__(processador, memoria)
        self.bateria:float = bateria

    def __str__(self):
        return f"LAPTOP / PROCESSADOR:{self.processador} / MEMORIA:{self.memoria} / Bateria:{self.bateria} WATTS"


class Desktop(Computador):
    def __init__(self, processador, memoria, gabinete=""):
        super().__init__(processador, memoria)
        self.gabinete:str = gabinete

    def __str__(self):
        return f"DESKTOP / PROCESSADOR:{self.processador} / MEMORIA:{self.memoria} / Gabinete:{self.gabinete}"


comp = Computador("NAO ENTENDO",13)

lap = Laptop("SLA",64,35)

desk = Desktop("so Deus sabe",78,"magico")

print(comp)
print(lap)
print(desk)
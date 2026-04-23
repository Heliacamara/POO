class Computador:
    def __init__(self,processador,memoria):
        self.processador:str=processador
        self.memoria:int=memoria

class Laptop(Computador):
    def __init__(self, processador,memoria,bateria_watts=0):
        super().__init__(processador,memoria)
        self.bateria_watts:int=bateria_watts 

    def mostrar_laptop(self): 
        print(f"Laptop: {self.processador}, {self.memoria}GB, bateria: {self.bateria_watts}W")

class Desktop(Computador):
    def __init__(self, processador,memoria,gabinete=""):  
        super().__init__(processador,memoria)
        self.gabinete:str=gabinete

    def mostrar_desktop(self):
        print(f"Desktop: {self.processador}, {self.memoria}GB, gabinete: {self.gabinete}")

comp1=Laptop("Ryzen 7",4,54)
comp1.mostrar_laptop()
comp2=Desktop("Do bom",32,"FULL-TOWER")
comp2.mostrar_desktop()

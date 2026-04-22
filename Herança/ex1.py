class Computador:
    def __init__(self,processador,memoria):
        self.processador:str=processador
        self.memoria:int=memoria

class Laptop(Computador):
   def __init__(self, processador, memoria,bateria_watts=0):
       super().__init__(processador, memoria)
       self.bateria_watts:int=0

def mostrar_laptop(self):
       pass
   
class Desktop(Computador):
    def __init__(self, processador, memoria,gabinete):
        super().__init__(processador, memoria)
        self.cabinete:str=gabinete
                
    def mostrar_desktop(self):
        pass            
comp1=Laptop("Ryzen 7",4,54)
comp2=Desktop("Do bom",32,"FULL-TOWER")

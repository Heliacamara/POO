class Forma:
    def area(self):
        return "0"
    
class Retangulo(Forma):
    def __init__(self,largura,altura):
       self.largura:float=largura
       self.altura:float=altura        

    def calcular(self):
        return self.altura*self.largura
        
ret=Retangulo(12,12)

print(f"A area do retangulo:{ret.calcular()}")
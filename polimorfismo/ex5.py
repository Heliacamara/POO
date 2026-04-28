from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self,raio):
        self.raio=raio

    def calcular_area(self):
        return math.pi * self.raio * self.raio

class Retangulo(Forma):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return self.base*self.altura

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return (self.base*self.altura) / 2

formas=[Circulo(2),Retangulo(2, 4),Triangulo(5, 10)]

for f in formas:
    print(f.calcular_area())
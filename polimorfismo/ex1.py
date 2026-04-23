class Animal:
    def emitir_som(self):
        return "Algum som generico"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
    
class Gato(Animal):
    def imitar_som(self):
        return "Miado"
    
    
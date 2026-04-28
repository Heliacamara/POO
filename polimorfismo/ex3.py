class Animal:
    def emitir_som(self):
        return "Algum som generico"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miado"
    
animals= [Cachorro(),Gato(),Animal()]
#for animal in animals:
    #print(animal.emitir_som())

print(animals[0].emitir_som())
print(animals[1].emitir_som())
print(animals[2].emitir_som())
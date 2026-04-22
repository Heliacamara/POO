class Animal:
    def fazer_som(self):
        return "Som do animal"

class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"
    
auau1=Cachorro()
print(auau1.fazer_som())


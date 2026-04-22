class Animal:
    def __init__(self,grupo):
        self.grupo:str=grupo

class Cachorro(Animal):
    def __init__(self):
        super().__init__("mamifero")

auau=Cachorro()
print(auau.grupo)
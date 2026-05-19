class Paciente:
    def __init__(self,nome,cpf,idade):
        self.nome=nome
        self.cpf:int=cpf
        self.__idade:int=idade
        
    @property
    def idade(self):
        return self.__idade   
    @idade.setter
    def idade(self,idade):
        if self.__idade>0:
            self.__idade=idade
        else:
            print("A idade nao pode ser negativa")    

class Medico:
    def __init__(self,nome,crm,especialidade):
        self.nome=nome
        self.crm=crm
        self.especialidade=especialidade
        
    def __str__(self):    
        return f"Nome: {self.nome}| CRM:{self.crm}| ESPECIALIDADE:{self.especialidade}"
    
p1 = Paciente("Helia", "12345678900", 15)
m1 = Medico("Dr. João", "CRM123", "Pediatria")

# testando getter
print("Idade paciente:", p1.idade)

# testando setter válido
p1.idade = 16
print("Nova idade:", p1.idade)

# testando setter inválido
p1.idade = -5

print()

# testando médico (__str__)
print(m1)
class Paciente:
    def __init__(self, nome,cpf,contato,data_nascimento):
        self.nome=nome
        self.contato=contato
        self.data_nascimento=data_nascimento
        self.__cpf=None
        self.cpf=cpf  

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf_outro):
        if len(str(cpf_outro))== 11:
            self.__cpf =cpf_outro
        else:
            print("Erro: CPF deve conter 11 dígitos")

    def __str__(self):
        return f"Nome: {self.nome} | CPF:{self.cpf}"
    
paci=Paciente("Joata","123145196778","7346447438","98760954")
print(paci)    
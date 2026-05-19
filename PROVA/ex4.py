class Pessoa:
    def __init__(self,nome,endereco):
        self.nome=nome
        self.endereco=endereco

class Medico(Pessoa):
    def __init__(self, nome, endereco,especialidade,crm):
        super().__init__(nome, endereco)
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f"Medico: {self.nome} | CRM: {self.crm} | ESPECIALIDADE: {self.especialidade}"
    
class MedicoEspecialista(Medico):
    def __init__(self, nome, endereco, especialidade, crm,registro_especialidade):
        super().__init__(nome, endereco, especialidade, crm)    
        self.registro_especialidade=registro_especialidade

    def apresentar_medico(self):
         return f"Medico: {self.nome}  CRM: {self.crm} | ESPECIALIDADE: {self.especialidade}| REGISTRO DE ESPECIALIDADE: {self.registro_especialidade}"    
    
class Paciente(Pessoa):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf


medico_regular = Medico("Dr. Rafa", "Natal", "Geral", "1873")
medico_especialista = MedicoEspecialista("Dra. Paula", "IFCM", "Cardiologista", "764", "RQE-34")

corpo_clinico = [medico_regular, medico_especialista]
for med in corpo_clinico:
    print(med.apresentar_medico())
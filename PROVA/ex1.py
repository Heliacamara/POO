class Medico:
    def __init__(self,nome,especialidade,crm):
        self.nome=nome
        self.especialidade=especialidade
        self.crm=crm

    def apresentar_medico(self):
        return f"Nome: {self.nome}| CRM:{self.crm}| ESPECIALIDADE:{self.especialidade}"

class Paciente:
    def __init__(self,nome,cpf,contato,data_nascimento):
        self.nome=nome
        self.cpf:int=cpf
        self.contato=contato
        self.data_nascimento:int=data_nascimento

    def exibir_informacoes(self):
        return f"Nome: {self.nome}| CPF:{self.cpf}| DATA DE NASCIMENTO:{self.data_nascimento}"     
    
pac=Paciente("Helia","12423536645","744646464",12112008)
print(pac.exibir_informacoes())
med=Medico("Dr. Helia","cardiologista",65453)
print(med.apresentar_medico())



class Clinica:
    def __init__(self,nome_unidade):
        self.nome_unidade=nome_unidade
        self.__corpo_clinico=[]
        self.__lista_pacientes=[]

    def adicionar_medico(self,medico):
        self.__corpo_clinico.append(medico)

    def adicionar_paciente(self,paciente):
        self.__lista_pacientes.append(paciente)

class Agendamento:
    def __init__(self,medico,paciente,data_hora):
        self.medico=medico
        self.paciente=paciente
        self.data_hora=data_hora



      

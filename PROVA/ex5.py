from abc import ABC,abstractmethod

class DocumentoSaude(ABC):
    @abstractmethod
    def gerar_relatorio(self):
        pass

class PacienteNaoCadastradoError(Exception):
    pass

class Agendamento(DocumentoSaude):
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    def gerar_relatorio(self):
        return f"Médico: {self.medico.nome} | Paciente: {self.paciente.nome} | Horário: {self.data_hora}"

class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        self.__lista_pacientes = []

    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.__lista_pacientes:
            if paciente.cpf == cpf:
                return paciente
        raise PacienteNaoCadastradoError(f"Paciente com CPF {cpf} não cadastrado.")


clinica = Clinica("Unidade Central")

try:
    clinica.buscar_paciente_por_cpf("00000000000")
except PacienteNaoCadastradoError as erro:
    print(f"Exceção capturada: {erro}")
from abc import ABC, abstractmethod


class PacienteNaoEncontradoError(Exception):
    pass


class PessoaClinica(ABC):
    @abstractmethod
    def get_identificacao(self):
        pass

class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Medico(PessoaClinica):
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm
        self.pacientes = []

    def get_identificacao(self):
        return f"Médico: {self.nome} - CRM: {self.crm}"

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                return paciente
        raise PacienteNaoEncontradoError("Paciente não encontrado!")


# ================= TESTE DIRETO =================

medico = Medico("Dr. Carlos", "12345")

p1 = Paciente("Ana", "111")
p2 = Paciente("João", "222")

medico.pacientes.append(p1)
medico.pacientes.append(p2)

print(medico.get_identificacao())
print("-" * 30)

try:
    paciente = medico.buscar_paciente_por_cpf("111")
    print("Encontrado:", paciente.nome)
except PacienteNaoEncontradoError as e:
    print("Erro:", e)

print("-" * 30)

try:
    paciente = medico.buscar_paciente_por_cpf("999")
    print("Encontrado:", paciente.nome)
except PacienteNaoEncontradoError as e:
    print("Erro:", e)
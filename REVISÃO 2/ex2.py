class Clinica:
    def __init__(self,nome):
        self.nome=nome
        self.lista_pacientes=[]
        self.lista_medicos=[]
        
    def adicionar_paciente(self,pacientes):
        self.lista_pacientes.append(pacientes)

    def adicionar_medico(self,medicos):
        self.lista_medicos.append(medicos)

class Consulta:
    def __init__(self, paciente, medico, data_consulta, horario):
        self.paciente = paciente
        self.medico = medico
        self.data_consulta = data_consulta
        self.horario = horario

    def exibir_consulta(self):
        return (f"Paciente: {self.paciente.nome} | "
                f"Médico: {self.medico.nome} | "
                f"Data: {self.data_consulta} | Horário: {self.horario}")

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Medico:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("Helia")
m1 = Medico("Dr. João")
clinica = Clinica("Central")
clinica.adicionar_paciente(p1)
clinica.adicionar_medico(m1)
consulta = Consulta(p1, m1, "19/05/2026", "14:00")
print(consulta.exibir_consulta())


#Ela usa objetos externos (Paciente e Medico)
#Esses objetos não dependem da consulta para existir
#Se apagar a consulta, paciente e médico continuam existindo
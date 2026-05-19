class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm

    def exibir_dados(self):
        return f"Médico: {self.nome} - CRM: {self.crm}"


class Clinica:
    def __init__(self):
        # dicionário: chave = CRM, valor = objeto Médico
        self.lista_medicos = {}

    def adicionar_medico(self, medico):
        self.lista_medicos[medico.crm] = medico

    def buscar_medico_por_crm(self, crm):
        return self.lista_medicos.get(crm, None)
    
clinica = Clinica()

m1 = Medico("Dr. Carlos", "123")
m2 = Medico("Dra. Ana", "456")

clinica.adicionar_medico(m1)
clinica.adicionar_medico(m2)

# busca existente
medico = clinica.buscar_medico_por_crm("123")
if medico:
    print(medico.exibir_dados())

print("-" * 30)

# busca inexistente
medico = clinica.buscar_medico_por_crm("999")
if medico:
    print(medico.exibir_dados())
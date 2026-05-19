class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")


class Paciente(Pessoa):
    def __init__(self, nome, telefone, cpf):
        super().__init__(nome, telefone)
        self.cpf = cpf

    def exibir_dados(self):
        super().exibir_dados()
        print(f"CPF: {self.cpf}")


class Consulta:
    def __init__(self, paciente, data):
        self.paciente = paciente
        self.data = data

    def exibir_dados(self):
        print(f"Data da consulta: {self.data}")
        self.paciente.exibir_dados()


class ConsultaOnline(Consulta):
    def __init__(self, paciente, data, plataforma):
        super().__init__(paciente, data)
        self.plataforma = plataforma

    def exibir_dados(self):
        print("=== Consulta Online ===")
        print(f"Plataforma: {self.plataforma}")
        super().exibir_dados()


# =========================
# TESTE (POLIMORFISMO)
# =========================

p1 = Paciente("Helia", "983377", "171636454")

c1 = Consulta(p1, "20/05/2026")
c2 = ConsultaOnline(p1, "21/05/2026", "Zoom")

lista_consultas = [c1, c2]

for consulta in lista_consultas:
    consulta.exibir_dados()
    print("-" * 30)
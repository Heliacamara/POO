class Pessoa:

    def __init__(self,nome,endereco):
        self.nome=nome
        self.endereco=endereco


class Membro(Pessoa):
    def __init__(self,nome,endereco,id_membro,contato,data_cadastro):
        super().__init__(nome,endereco)
        self.id_membro=id_membro
        self.contato=contato
        self.data_cadastro=data_cadastro

    def exibir_detalhes(self):
        print(f"Quem pegou o livro: {self.nome}")
        print(f"Endereco: {self.endereco}")
        print(f"Id_membro: {self.id_membro}")
        print(f"Contato: {self.contato}")
        print(f"Data de cadastro: {self.data_cadastro}")

p1=Membro("Helia","Rua A",10,"helia@gmail.com","18/05/2026")

p1.exibir_detalhes()
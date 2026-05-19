class Paciente:
    def __init__(self,nome,cpf,idade):
        self.nome=nome
        self.cpf:int=cpf
        self.idade:int=idade

    def exibir_dados(self):
        return f"Nome: {self.nome}| CPF:{self.cpf}| IDADE:{self.idade}"
            
class Medico:
    def __init__(self,nome,crm,especialidade):
        self.nome=nome
        self.crm=crm
        self.especialidade=especialidade

p1=Paciente("Helia","18767898545",15)
print(p1.exibir_dados())

#__init__: é um método especial chamado automaticamente quando um objeto é criado. Ele serve para inicializar os atributos da classe, ou seja, definir os valores iniciais do objeto.
#self: representa o próprio objeto que está sendo criado ou manipulado. Ele permite acessar os atributos e métodos dentro da classe.

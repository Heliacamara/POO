class ContaCorrente:
    def __init__(self,nome_correntista,cpf_correntista,saldo):
        self.nome_correntista =nome_correntista
        self.cpf_correntista= cpf_correntista
        self.saldo= saldo
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        self.saldo -= valor
    def mostrar_saldo(self):
        print(f'Nome:{self.nome_correntista}')
        print(f'CPF:{self.cpf_correntista}')
        print(f'Saldo atual:{self.saldo:.2f}')
corrente = ContaCorrente('Pedro','234.456.678-34',200)
corrente.sacar(200)
corrente.depositar(100)
corrente.mostrar_saldo()
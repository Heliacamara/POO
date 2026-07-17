class Endereço:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = int(numero)
        self.__bairro = bairro
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self.__bairro

    def get_cidade(self):
        return self.__cidade

    def exibir_dados(self):
        return f'Rua: {self.__rua}, Numero: {self.__numero}\nBairro: {self.__bairro}\nCidade: {self.__cidade}'


class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__contas = []

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def exibir_dados(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\n{self.__endereco.exibir_dados()}'

    def possui_contas(self):
        if len(self.__contas)==1 or len(self.__contas)>1:
            return True
        else:
            return False

    def buscar_conta(self,numero):
        for conta in self.__contas:
            if conta.get_numero()==numero:
                return conta

        return None

    def consultar_saldo_total(self):
        total=0
        for conta in self.__contas:    
                total= total + conta.get_saldo()
        return total

class ContaBancaria:

    numeros_contas = []

    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(numero)

    def get_titular(self):
        return self.__titular.get_nome()

    def get_numero(self):
        return self.__numero

    def get_tipo_conta(self):
        return "Conta Bancária"

    def get_saldo(self):
        return self.__saldo

    @classmethod
    def verificar_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))

    @classmethod
    def contas_duplicadas(cls):
        repetidos = set()
        for numero in cls.numeros_contas:
            if cls.numeros_contas.count(numero) > 1:
                repetidos.add(numero)
        return repetidos

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False

    def exibir_dados(self):
        return (
            f'CONTA\n'
            f'Titular: {self.__titular.get_nome()}\n'
            f'Numero: {self.__numero}\n'
            f'Saldo: R$ {self.__saldo}\n'
            f'CPF: {self.__titular.get_cpf()}\n\n'
            f'ENDEREÇO\n'
            f'{self.__titular.get_endereco().exibir_dados()}'
        )
    


class ContaCorrente(ContaBancaria):

    def __init__(self, titular, numero, saldo, limite, tarifa_mensal):
        super().__init__(titular, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal

    def sacar(self, valor):
      if valor > 0 and valor <= self._ContaBancaria__saldo + self.__limite:
        self._ContaBancaria__saldo -= valor
        return True
      return False

    def cobrar_tarifa(self):
        return self.sacar(self.__tarifa_mensal)

    def get_tipo_conta(self):
        return "Conta Corrente"

    def exibir_dados(self):
        return (
            f'{super().exibir_dados()}\n'
            f'Limite: R$ {self.__limite}\n'
            f'Tarifa mensal: R$ {self.__tarifa_mensal}'
        )


class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, numero, saldo, taxa_rendimento):
        super().__init__(titular, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def get_tipo_conta(self):
        return "Conta Poupança"

    def render_juros(self):
        self._ContaBancaria__saldo += (
            self._ContaBancaria__saldo * self.__taxa_rendimento
        )

    def exibir_dados(self):
        return (
            f'{super().exibir_dados()}\n'
            f'Taxa de rendimento: {self.__taxa_rendimento * 100}%'
        )


class ContaSalario(ContaBancaria):

    def __init__(self, titular, numero, saldo, empresa, saques_realizados, limite_saques):
        super().__init__(titular, numero, saldo)
        self.__empresa = empresa
        self.__saques_realizados = saques_realizados
        self.__limite_saques = limite_saques

    def receber_salario(self, valor):
        if valor > 0:
            self._ContaBancaria__saldo += valor
            return True
        return False

    def depositar(self, valor):
        print("Depositos comuns nao sao permitidos.")
        return False

    def sacar(self, valor):
        if self.__saques_realizados >= self.__limite_saques:
            print("Limite de saques atingido.")
            return False

        if valor > 0 and valor <= self._ContaBancaria__saldo:
            self._ContaBancaria__saldo -= valor
            self.__saques_realizados += 1
            return True

        return False

    def get_tipo_conta(self):
        return "Conta Salário"

    def transferir(self, valor, conta_destino):
        print("Tente novamente,transferencias nao sao permitidas para Conta Salario.")
        return False

    def exibir_dados(self):
        return (
            f'{super().exibir_dados()}\n'
            f'Empresa: {self.__empresa}\n'
            f'Saques realizados: {self.__saques_realizados}\n'
            f'Limite de saques: {self.__limite_saques}'
        )

class ContaUniversitaria(ContaBancaria):
    def __init__(self, titular, numero, saldo):
        super().__init__(titular, numero, saldo)

    def get_tipo_conta(self):
        return "Conta Univeritaria"

    def sacar(self, valor):
        if valor <= 500:
            return super().sacar(valor)

        return False



#testando possuir conta
endereco=Endereço("Rua A", 10, "Centro", "Natal")

cliente=Cliente("Maria", "12345678900", endereco)

print(cliente.possui_contas())

conta = ContaCorrente(cliente, 1, 1000, 500, 20)

cliente.adicionar_conta(conta)

print(cliente.possui_contas())


#testando consultar saldo
cliente = Cliente("Maria", "12345678900", endereco)

conta1 = ContaCorrente(cliente, 101, 500, 200, 10)
conta2 = ContaPoupanca(cliente, 202, 1000, 0.02)

cliente.adicionar_conta(conta1)
cliente.adicionar_conta(conta2)

print(cliente.consultar_saldo_total())

#testar Conta Universitaria
# Criando endereço
endereco = Endereço("Rua A", 100, "Centro", "Natal")

# Criando cliente
cliente = Cliente("Maria", "12345678900", endereco)

# Criando conta universitária com saldo de 1000
conta_uni = ContaUniversitaria(cliente, 101, 1000)

# Adicionando conta ao cliente
cliente.adicionar_conta(conta_uni)


# Teste 1 - Ver tipo da conta
print(conta_uni.get_tipo_conta())


# Teste 2 - Saque permitido (menor que 500)
resultado = conta_uni.sacar(300)

print("Saque de 300:", resultado)
print("Saldo atual:", conta_uni.get_saldo())


# Teste 3 - Saque no limite máximo
resultado = conta_uni.sacar(500)

print("Saque de 500:", resultado)
print("Saldo atual:", conta_uni.get_saldo())


# Teste 4 - Saque acima do limite
resultado = conta_uni.sacar(600)

print("Saque de 600:", resultado)
print("Saldo atual:", conta_uni.get_saldo())


# Teste 5 - Saque maior que o saldo disponível
resultado = conta_uni.sacar(1000)

print("Saque de 1000:", resultado)
print("Saldo atual:", conta_uni.get_saldo())
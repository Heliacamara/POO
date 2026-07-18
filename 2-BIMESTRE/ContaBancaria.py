class Endereco:
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
    def __init__(self,nome,cpf,rua,numero,bairro,cidade):
        self.__nome = nome
        self.__cpf = cpf 
        self.__endereco = Endereco(rua,numero,bairro,cidade)
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
        pass

class ContaBancaria:
    numeros_contas = []
    contas_duplicada = []
    def __init__(self,cliente,numero,saldo):
        self.__cliente = cliente 
        self.__numero =  numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(self.__numero)
    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))
    @classmethod
    def contas_duplicadas(cls):
        vistos = set()
        for numero in cls.numeros_contas:
            if numero in vistos:
                cls.contas_duplicada.append(numero)
            else:
                vistos.add(numero)
        return cls.contas_duplicada
    def get_cliente(self):
        return self.__cliente
    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,valor):
        self.__saldo = valor 
        
    
    def get_tipo_conta(self):
        return "Conta Bancária"
    def depositar(self,valor):
        self.__saldo += valor
        return True
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False
    def transferir(self,valor,destino):
            if self.sacar(valor):
                destino.depositar(valor)
                return True
            else:
                return False

    def exibir_dados(self):
        return (
            f'CONTA\n'
            f'Titular: {self.__cliente.get_nome()}\n'
            f'Numero: {self.__numero}\n'
            f'Saldo: R$ {self.__saldo}\n'
            f'CPF: {self.__cliente.get_cpf()}\n\n'
            f'ENDEREÇO\n'
            f'{self.__cliente.get_endereco().exibir_dados()}'
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

# endereco=Endereco("Rua A", 10, "Centro", "Natal")

# cliente=Cliente("Maria", "12345678900", endereco)

# print(cliente.possui_contas())

# conta = ContaCorrente(cliente, 1, 1000, 500, 20)

# cliente.adicionar_conta(conta)

# print(cliente.possui_contas())
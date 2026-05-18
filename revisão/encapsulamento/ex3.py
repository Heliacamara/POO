class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo=saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor


c1 = ContaBancaria(500)

c1.depositar(200)
c1.sacar(100)

print("Saldo:", c1.saldo)
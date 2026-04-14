class ContaBancaria:
    def __init__(self,titular):
        self.__saldo= 0

    def get__saldo(self):
        return self.__saldo    

    def set_saldo(self,valor):
        if valor > 0:
            self.__saldo=valor
        else:
            print("Saldo está indisponivel")

    def depositar(self,valor):
        if valor > 0:
            self.__saldo +=valor
        else:
             print("Valor indisponivel para depositar.")
                 
    def sacar(self,valor):
        if valor <= self.__saldo:
                self.__saldo -=valor
        else:
             print("Saldo indisponivel")



conta= ContaBancaria("Maria")

conta.depositar(500)
conta.sacar(200)

print("Saldo atual:",conta.get__saldo())
conta.set_saldo(0)
print("Saldo atual:",conta.get__saldo())
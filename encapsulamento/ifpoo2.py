class ContaBancaria:
    def __init__(self,titular):
        self.titular= titular
        self.__saldo= 0

    @property
    def saldo(self):
        return self.__saldo    

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

    def consultar_saldo(self):
        return self.__saldo


conta= ContaBancaria("Maria")

conta.depositar(500)
conta.sacar(200)

print("Saldo atual:",conta.consultar_saldo())
                  
          
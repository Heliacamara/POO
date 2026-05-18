class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.__saldo=saldo

    def depositar(self,valor):
        if valor >0:
            self.__saldo+=valor
        else:
             print("Nao e possivel depositar valores menor ou igual a zero")   
        

    def sacar(self,valor):
        if valor <=self.__saldo:
           self.__saldo-=valor
        else:
             print("O saque não pode ser maior que o saldo disponivel")
 
    def consultar_saldo(self):
        return self.__saldo

p1= ContaBancaria("Marilia",0)    
p1.depositar(500)
p1.sacar(200)
print("Saldo atual:",p1.consultar_saldo())    
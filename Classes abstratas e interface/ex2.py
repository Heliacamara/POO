from abc import ABC,abstractmethod

class DispositivosEletronicos(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carregavel(ABC):
    @abstractmethod
    def carregar(self):
        pass

class Smartphone(DispositivosEletronicos,Carregavel):
    def ligar(self):
       return "O Smartphone esta ligando" 
   
    def desligar(self):
        return "Este Smartphone esta desligando"
    
    def carregar(self):
        return("O Smartphone esta precisando carregar")
    

class Notebook(DispositivosEletronicos,Carregavel):
    def ligar(self):
       return "O Notebook esta ligando" 
   
    def desligar(self):
        return "Este Notebook esta desligando"
    
    def carregar(self):
        return("O Notebook esta precisando carregar")
    

class FoneDeOuvido(DispositivosEletronicos):
    def ligar(self):
       return "O fone de ouvido esta ligando" 
   
    def desligar(self):
        return "Este fone de ouvido esta desligando"
    

dispositivosEletronicos= [Smartphone(),Notebook(),FoneDeOuvido()]
dispositivosCarregaveis=[Smartphone(),Notebook()]

for aparelhos in dispositivosEletronicos:
    print()
    print(aparelhos.ligar())
    print(aparelhos.desligar())

for carrega in dispositivosCarregaveis:
    print()
    print(carrega.carregar())    
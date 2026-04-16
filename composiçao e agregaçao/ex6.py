class Comodo:
    def __init__(self,nome,tamanho):
        self.nome=nome
        self.tamanho:int=tamanho

class Casa:
    def __init__(self):
        self.lista_de_comodos=[]
    
    def adicionar_comodo(self,nome,tamanho):
        comodo = Comodo(nome,tamanho)
        self.lista_de_comodos.append(comodo)

    def listar_comodos(self):
        for comodo in self.lista_de_comodos:
            print(f"O {comodo.nome} tem o tamanho {comodo.tamanho} metros quadrados")

casa=Casa()
casa.adicionar_comodo("Quarto",56)  
casa.adicionar_comodo("Cozinha",70)
casa.listar_comodos()           


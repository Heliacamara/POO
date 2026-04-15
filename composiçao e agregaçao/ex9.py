class ItemPedido:
    def __init__(self,produto,quantidade,preco):
        self.produto=produto
        self.quantidade:int=quantidade
        self.preco:int=preco

    def __str__(self):
        return f"O produto: {self.produto}, Quantidade: {self.quantidade},Preco:{self.preco}"
class Pedido:
    def __init__(self):
        self.lista_de_itens=[]
    
    def adicionar_item(self, item):
        self.lista_de_itens.append(item)

    def calcular_total(self):
        soma_total=0
        for produto in self.lista_de_itens:
            soma_total+= produto.preco
        print(f"A soma dos itens:{soma_total}")

    def mostrar(self):
        for item in self.lista_de_itens:
            print(f"{item}")                                    
ob1=ItemPedido("Carro",1,100.000)        
ob2=ItemPedido("Casa",2,150.000)
pedi=Pedido()
pedi.adicionar_item(ob1)
pedi.adicionar_item(ob2)
pedi.mostrar()
pedi.calcular_total( )

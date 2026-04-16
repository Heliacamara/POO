class ItemPedido:
    def __init__(self,produto,quantidade,preco):
        self.produto=produto
        self.quantidade:int=quantidade
        self.preco:int=preco

    def __str__(self):
        return f"O produto: {self.produto}; Quantidade: {self.quantidade}; Preco: {self.preco}"

class Pedido:
    def __init__(self):
        self.lista_de_itens=[]

    def adicionar_item(self,produto,quantidade,preco):
        item=ItemPedido(produto,quantidade,preco)
        self.lista_de_itens.append(item)

    def calcular_total(self):
        soma_total=0
        for produto in self.lista_de_itens:
            soma_total += produto.preco * produto.quantidade
        print(f"A soma dos produtos: {soma_total}")

    def mostrar(self):
        for item in self.lista_de_itens:
            print(item)

pedi = Pedido()
pedi.adicionar_item("Carro", 1, 100000)
pedi.adicionar_item("Casa", 2, 150000)
pedi.mostrar()
pedi.calcular_total()
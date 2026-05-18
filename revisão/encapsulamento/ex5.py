class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_em_estoque = quantidade_em_estoque

    def vender(self, quantidade):
        if quantidade <= self.__quantidade_em_estoque:
            self.__quantidade_em_estoque -= quantidade
            print("Venda realizada")
        else:
            print("Nao tem quantidade disponivel no estoque")

    def repor_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_em_estoque += quantidade
        else:
            print("Nao e possivel adicionar ao estoque")

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def quant_estoq(self):
        return self.__quantidade_em_estoque


p1 = Produto("Celular", 3000, 2)

p1.vender(1)

p1.repor_estoque(3)

print("Nome:", p1.nome)
print("Preco:", p1.preco)
print("Estoque:", p1.quant_estoq)
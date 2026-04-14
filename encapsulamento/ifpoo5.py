# class Produto:
#     def __init__(self,nome,preco,quantidade_inicial_do_produto):
#         self.__nome:str=nome
#         self.__preco:float=preco
#         self.__quantidade_em_estoque:int= quantidade_inicial_do_produto

#     def vender(self,valor):
#        if self.__quantidade_em_estoque == valor:
#             self.__quantidade_em_estoque-valor
#        else:
#            print("Não tem quantidade suficiente no estoque")

#     def repor_estoque(self,valor):
#      if valor>0:   
#         self.__quantidade_em_estoque += valor
#      else:
#         print("Não tem como adicionar")

#     def get__nome(self):
#        return self.__nome

#     def get__preco(self):
#        return self.__preço
    
#     def get_quantidade_em_estoque(self):
#        return self.__quantidade_em_estoque


# cliente= Produto("Bolo",30,2)
# cliente.vender(2)
# cliente.repor_estoque(4)

# print("Nome do produto:", cliente.get__nome())
# cliente.get__nome()
# print("Preço do produto:",cliente.get__preco())
# cliente.get__preco("50")
# print("Quantidade atual do estoque:", cliente.get_quantidade_em_estoque())

                   #PRIMEIRA VERSÃO DA QUESTÃO A CIMA

# class Produto:
#     def __init__(self, nome, preco, quantidade_inicial_do_produto):
#         self.__nome=nome
#         self.__preco=preco
#         self.__quantidade_em_estoque=quantidade_inicial_do_produto

#     def vender(self, quantidade):
#         if quantidade <= self.__quantidade_em_estoque:
#             self.__quantidade_em_estoque -=quantidade
#         else:
#             print("Quantidade insuficiente no estoque")

#     def repor_estoque(self, quantidade):
#         if quantidade > 0:
#             self.__quantidade_em_estoque +=quantidade
#         else:
#             print("Nao tem como adicionar")

#     def get_nome(self):
#         return self.__nome

#     def get_preco(self):
#         return self.__preco

#     def get_quantidade_em_estoque(self):
#         return self.__quantidade_em_estoque


# cliente= Produto("Lapis", 12, 4)

# cliente.vender(10)
# cliente.repor_estoque(0)

# print("Nome do produto:", cliente.get_nome())
# print("Preco do produto:", cliente.get_preco())
# print("Quantidade atual do estoque:", cliente.get_quantidade_em_estoque())
                # SEGUNDA VERSÃO A CIMA 

                #BÔNUS DA QUESTÃO A BAIXO


class Produto:
    def __init__(self, nome, preco, quantidade_inicial_do_produto):
        self.__nome=nome
        self.__preco=preco
        self.__quantidade_em_estoque=quantidade_inicial_do_produto

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,valor):
        if valor <= 0:
            self.__preco=valor
        else:
            print("O preço nao pode ser negativo")

    @property
    def quantidade_em_estoque(self):
        return self.__quantidade_em_estoque

    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self,valor):
        if valor <= 0:
            self.__quantidade_em_estoque=valor
        else:
            print("A quantidade nao pode ser negativa")

    def vender(self,quantidade):
        if quantidade <=self.__quantidade_em_estoque:
            self.__quantidade_em_estoque -=quantidade
        else:
            print("Nao tem quantidade suficiente")

    def repor_estoque(self,quantidade):
        self.__quantidade_em_estoque += quantidade

    def get_nome(self):   
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque


produto = Produto("Lapis", 12,6)

produto.vender(6)
produto.repor_estoque(5)

print("Nome:", produto._Produto__nome)  
print("Preco:", produto.preco)
print("Quantidade:", produto.quantidade_em_estoque)
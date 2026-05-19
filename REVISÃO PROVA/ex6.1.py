class Membro:
    def __init__(self, id_membro, nome):
        self.id_membro = id_membro
        self.nome = nome

    def exibir_dados(self):
        print(f"ID: {self.id_membro}")
        print(f"Nome: {self.nome}")


class Biblioteca:
    def __init__(self):
        # Agora é um dicionário: chave = id_membro, valor = objeto Membro
        self.lista_membros = {}

    def adicionar_membro(self, membro):
        # Usa o id_membro como chave do dicionário
        self.lista_membros[membro.id_membro] = membro

    def buscar_membro_por_id(self, id_membro):
        # Retorna o membro se existir, senão retorna None
        return self.lista_membros.get(id_membro, None) #O get() serve para acessar valores de um dicionário de forma segura. #dicionario.get(chave, valor_padrao)    
    
bib = Biblioteca()

m1 = Membro(1, "Ana")
m2 = Membro(2, "Carlos")

bib.adicionar_membro(m1)
bib.adicionar_membro(m2)

busca = bib.buscar_membro_por_id(2)

if busca:
    print("Membro encontrado:")
    busca.exibir_dados()
else:
    print("Membro não encontrado")


#O dicionário é mais eficiente porque permite acessar o membro diretamente pelo id_membro, sem precisar percorrer todos os elementos, tornando a busca muito mais rápida e eficiente que em uma lista.
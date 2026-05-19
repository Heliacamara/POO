agenda={}

def adicionar_contato(agenda,nome,telefone):
    agenda[nome]=telefone
    print("Contato salvo")

def buscar_telefone(agenda,nome):
    if nome in agenda:
        return f"Telefone de {nome}: {agenda[nome]}"
    else:
        return "Contato nao identificado"

def remover_contato(agenda,nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido")
    else:
        print("Contato nao encontrado")

def listar_contatos(agenda):
    if len(agenda)==0:
        print("Agenda vazia")
    else:
        print("\n-- CONTATOS --")
        for nome,telefone in agenda.items():
            print(f"Nome: {nome} | Telefone: {telefone}")

while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1- Adicionar contato")
    print("2- Buscar telefone")
    print("3- Remover contato")
    print("4- Listar contatos")
    print("5- Sair")

    escolha=input("Escolha uma opcao:")

    if escolha=="1":
        nome=input("Digite o nome:")
        telefone=input("Digite o telefone:")
        adicionar_contato(agenda,nome,telefone)

    elif escolha=="2":
        nome=input("Digite o nome do contato:")
        print(buscar_telefone(agenda,nome))

    elif escolha=="3":
        nome=input("Digite o nome do contato para remover:")
        remover_contato(agenda,nome)

    elif escolha=="4":
        listar_contatos(agenda)

    elif escolha=="5":
        print("Programa encerrado")
        break

    else:
        print("Opcao invalida")
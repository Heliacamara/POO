anos={}

while True:
    nasceu= input("Digite o ano de nascimento:")
    if nasceu =="":
        break

    nasceu=int(nasceu)

    if nasceu in anos:
        anos[nasceu]+=1
    else:
        anos[nasceu]=1

print("\nDADOS")
for ano,quantidade in anos.items():
    print(f"Ano:{ano}| Quantidade de pessoa:{quantidade}")           
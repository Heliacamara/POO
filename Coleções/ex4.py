frase=input("Digite uma frase:")

frase=frase.lower()
frase=frase.replace(".","")
frase=frase.replace(",","")
frase=frase.replace("!","")
frase=frase.replace("?","")

palavras=frase.split()

unicas=set(palavras)

frequencia={}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra]+=1
    else:
        frequencia[palavra]=1

print("\nPalavras unicas:")
for palavra in sorted(unicas):
    print(palavra)

print("\nFrequencia das palavras:")
for palavra in sorted(frequencia):
    print(f"{palavra}: {frequencia[palavra]}")
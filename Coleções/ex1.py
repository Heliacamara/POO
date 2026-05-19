import random #Sorteia numeros aleatorios

sorteados=random.sample(range(1,41),25) #Gera numeros de 1 ate 40,25 numeros #SAMPLE-numeros aleatorios sem repetir

sorteados.sort()#Coloca os numeros em ordem crescente

print(f"Numero que foram sorteados:{sorteados}")

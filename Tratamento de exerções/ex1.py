def adicionar_valor(inicial,adicional):
    if adicional>0:
        return inicial+adicional
    else:
        raise ValueError("Somente valores positivos devem ser adicionados ao valor inicial")
    
try:
    resultado = adicionar_valor(8,4)
    print(f'Resultado: {resultado}')

except ValueError as erro:
    print(f'Erro: {erro}')

try:
    resultado = adicionar_valor(8,-4)
    print(f'Resultado: {resultado}')

except ValueError as erro:
    print(f'Erro: {erro}')
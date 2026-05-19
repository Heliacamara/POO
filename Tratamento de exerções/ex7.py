def verificar_nota(nota):
    if nota > 10 or nota < 0:
        raise ValueError("Nota inválida: deve estar entre 0 e 10")
    else:
        return "Nota correta"

try:
    print(verificar_nota(11))

except ValueError as erro:
    print(f"Erro: {erro}")

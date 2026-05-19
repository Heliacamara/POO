print("Abrindo arquivo...")
try:
    resulte=1/0
    print(f"Resultado:{resulte}")
except ZeroDivisionError:
    print("Erro na operacao")
finally:
    print("Fechando o arquivo...")
            
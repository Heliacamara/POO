def divisao_segura(a,b):
    try:
        return a/b
    
    except ZeroDivisionError:
        print("Erro:dvisao por zero")
        return None
    
    except TypeError:
        print("Erro:os valores devem ser numeros")
        return None

print(divisao_segura(10,2))
print(divisao_segura(5,0))
print(divisao_segura(4,"a"))    
        
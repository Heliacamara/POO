class SenhaCurtaError(Exception):
    pass

def cadastrar_senha(senha):
    if len(senha)<8:
        raise SenhaCurtaError("A senha deve obter ao menos 8 caracteres")
    else:
        return "Senha cadastrada"
try:
    print(cadastrar_senha("14680"))
except SenhaCurtaError as erro:
    print(f"Erro:{erro}")

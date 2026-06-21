import string
import random

def GeradorDeSenha():
    caracteres = string.ascii_letters + string.digits
    comprimento = 12

    senha = []
    for i in range (comprimento):
        caractere = random.choice(caracteres)
        senha.append(caractere)
    return ''.join(senha)

senha = GeradorDeSenha()
print(senha)
from utils_io import escrever, obter_numero_inteiro
from utils import validar_senha

def main():
    senha = obter_numero_inteiro('Insira sua senha: ')

    escrever(validar_senha(senha))


main()
from utils_io import escrever, obter_numero_inteiro
from utils import dezena_unidade

def main():
    numero = obter_numero_inteiro('Digite um número com dois algarismos: ')

    escrever(dezena_unidade(numero))


main()
from utils import verificar_iguais
from utils_io import obter_numero_real, escrever

def main():
    numero1 = obter_numero_real('Número 1: ')
    numero2 = obter_numero_real('Número 2: ')
    numero3 = obter_numero_real('Número 3: ')

    iguais = verificar_iguais(numero1, numero2, numero3)

    escrever(iguais)

main()
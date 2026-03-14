from utils_io import escrever, obter_numero_real
from utils import ordem_crescente

def main():
    numero1 = obter_numero_real('N1: ')
    numero2 = obter_numero_real('N2: ')
    numero3 = obter_numero_real('N3: ')

    escrever(ordem_crescente(numero1, numero2, numero3))


main()
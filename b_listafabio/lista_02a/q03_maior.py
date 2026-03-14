from utils_io import escrever, obter_numero_real
from utils import obter_maior

def main():
    numero1 = obter_numero_real('N1: ')
    numero2 = obter_numero_real('N2: ')
    numero3 = obter_numero_real('N3: ')

    maior = obter_maior(numero1, numero2, numero3)

    #if int(obter_maior(numero1, numero2, numero3)):
    #    escrever(f'Maior: {}')
    #else:
    #    escrever(maior)
    escrever(f'Maior: {maior}')


main()
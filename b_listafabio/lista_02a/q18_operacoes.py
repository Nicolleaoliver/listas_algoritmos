from utils_io import obter_numero_inteiro, obter_numero_real
from utils import operacoes

def main():
    valor1 = obter_numero_real('N1: ')
    valor2 = obter_numero_real('N2: ')
    operacao = obter_numero_inteiro('Escolha um operador (1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão): ')

    print(operacoes(valor1, valor2, operacao))


main()
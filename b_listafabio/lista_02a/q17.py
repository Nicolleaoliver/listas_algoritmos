from utils_io import obter_numero_inteiro
from utils import verificar_restos

def main():
    num1 = obter_numero_inteiro('N1: ')
    num2 = obter_numero_inteiro('N2: ')

    print(verificar_restos(num1, num2))


main()
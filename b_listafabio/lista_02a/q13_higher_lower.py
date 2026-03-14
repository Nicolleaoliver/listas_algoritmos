from utils_io import escrever, obter_numero_real
from utils import higher_lower

def main():
    escrever('Insira 5 números para ler qual o maior e o menor')
    num1 = obter_numero_real('N1: ')
    num2 = obter_numero_real('N2: ')
    num3 = obter_numero_real('N3: ')
    num4 = obter_numero_real('N4: ')
    num5 = obter_numero_real('N5: ')

    maior, menor = higher_lower(num1, num2, num3, num4, num5)
    
    escrever(f'O maior é {maior} e o menor é {menor}')


main()
from utils_io import escrever, obter_numero_real
from utils import media_maior

def main():
    escrever('Insira 5 números para saber a média e os que são maiores que a média')
    num1 = obter_numero_real('N1: ')
    num2 = obter_numero_real('N2: ')
    num3 = obter_numero_real('N3: ')
    num4 = obter_numero_real('N4: ')
    num5 = obter_numero_real('N5: ')

    media, maior = media_maior(num1, num2, num3, num4, num5)

    escrever(f'A média é {media} e o maior que a média é {maior}')


main()
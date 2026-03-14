from utils_io import escrever, obter_numero_inteiro
from utils import is_quadrado_perfeito

def main():
    num = obter_numero_inteiro('Número de 4 dígitos: ')

    codigo, dezena, dezena1 = is_quadrado_perfeito(num)

    if (dezena1 + dezena) ** 2 == num:
        escrever('Esse é um quadrado perfeito')
    else:
        escrever('Não é um quadrado perfeito')


main()
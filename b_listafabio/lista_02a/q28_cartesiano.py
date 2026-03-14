from utils_io import escrever, obter_numero_real
from utils import cartesiano

def main():
    escrever('>> Ponto 1: ')
    x1 = obter_numero_real('x1: ')
    y1 = obter_numero_real('y1: ')

    x2 = obter_numero_real('x2: ')
    y2 = obter_numero_real('y2: ')

    escrever(f'A área é {cartesiano(x1, y1, x2, y2)}')


main()
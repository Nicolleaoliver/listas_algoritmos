from utils_io import escrever, obter_numero_inteiro
from utils import is_quadrado_perfeito

def main():
    escrever('>> Vamos ver se seu número é um quadrado perfeito')
    num = obter_numero_inteiro('Número: ')

    if is_quadrado_perfeito(num):
        escrever(f'{num} É quadrado perfeito')
    else:
        escrever('Não é quadrado perfeito')


main()
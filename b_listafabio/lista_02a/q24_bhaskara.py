from utils_io import escrever, obter_numero_real
from utils import obter_delta, obter_raizes

def main():
    escrever('>>>Insira os valores de coeficientes a, b e c para calcular a equação de segundo grau<<<')
    a = obter_numero_real('> A: ')
    b = obter_numero_real('> B: ')
    c = obter_numero_real('> C: ')

    delta, mensagem = obter_delta(a, b, c)
    x1, x2 = obter_raizes(a, b, delta)

    if obter_raizes(a, b, delta) is not None:
        escrever(f'{mensagem} e as raízes são {x1} e {x2}')


main()
from utils_io import escrever, obter_numero_real
from utils import is_positive_negative

def main():
    num = obter_numero_real('Número: ')

    codigo = is_positive_negative(num)

    if codigo == 1:
        escrever('É positivo')
    else:
        escrever('É negativo')

main()



from utils_io import escrever, obter_numero_inteiro
from utils import par_impar

def main():
    numero = obter_numero_inteiro()

    if par_impar(numero):
        escrever('É par')
    else:
        escrever('É impar')


main()
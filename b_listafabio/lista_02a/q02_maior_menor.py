from utils_io import escrever, obter_numero_real
from utils import obter_maior_e_menor

def main():
    escrever('Insira dois números e verificarei qual o maior e qual o menor')
    numero1 = obter_numero_real('Número 1: ')
    numero2 = obter_numero_real('Número 2: ')

    resultado = obter_maior_e_menor(numero1, numero2)

    escrever(resultado)


main()
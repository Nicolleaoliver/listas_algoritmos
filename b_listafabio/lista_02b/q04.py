from utils_io import escrever, obter_numero_real
from utils import situacao_media

def main():
    nota1 = obter_numero_real('Nota 1: ')
    nota2 = obter_numero_real('Nota 2: ')

    escrever(situacao_media(nota1, nota2))


main()
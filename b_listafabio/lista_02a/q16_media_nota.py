from utils_io import escrever, obter_numero_real
from utils import media_nota

def main():
    nota1 = obter_numero_real('Nota 1: ')
    nota2 = obter_numero_real('Nota 2: ')

    escrever(media_nota(nota1, nota2))


main()
from utils_io import escrever, obter_numero_real
from utils import arredondar

def main():
    num = obter_numero_real('Número com casa decimal: ')

    escrever(f'Arredondando: {arredondar(num)}')

main()
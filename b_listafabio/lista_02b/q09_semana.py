from utils_io import escrever, obter_numero_inteiro
from utils import semana

def main():
    num = obter_numero_inteiro('Digite um número: ')

    escrever(semana(num))

main()
from utils_io import escrever, obter_numero_inteiro, obter_numero_real
from utils import obter_opcao

def main():
    #criar uma função menu depois
    escrever('>>> Insira 3 números <<<')
    num1 = obter_numero_real('> N1: ')
    num2 = obter_numero_real('> N2: ')
    num3 = obter_numero_real('> N3: ')

    escrever('> Agora escolha uma das opções (1, 2 ou 3) ')
    opcao = obter_numero_inteiro('> ')

    mostrar = obter_opcao(opcao, num1, num2, num3)
    escrever(mostrar)


main()
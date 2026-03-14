from utils_io import escrever, obter_numero_inteiro
from utils import eh_primo

def main():
    escrever('Insira um número de 0 a 100 e verificarei se ele é primo ou não')
    numero = obter_numero_inteiro('Número: ')

    primo = eh_primo(numero)
    escrever(primo)
    #if eh_primo(numero):
     #   escrever('Não é primo')
    #else:
     #   escrever(eh_primo(numero))


main()
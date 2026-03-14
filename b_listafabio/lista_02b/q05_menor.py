from utils_io import escrever, obter_numero_real
from utils import ordem_crescente

def main():
    produto1 = obter_numero_real('Preço do primeiro produto: ')
    produto2 = obter_numero_real('Preço do segundo produto: ')
    produto3 = obter_numero_real('Preço do terceiro produto: ')

    menor, meio, maior = ordem_crescente(produto1, produto2, produto3)

    if menor == produto1:
        escrever('Você deve comprar o primeiro produto')
    elif menor == produto2:
        escrever('Você deve comprar o segundo produto')
    elif menor == produto3:
        escrever('Você deve comprar o terceiro produto')


main()
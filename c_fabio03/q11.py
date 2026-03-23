def main():
    inferior = int(input('Limite inferior: '))
    superior = int(input('Limmite superior: '))

    obter_primos(inferior, superior)


def obter_primos(inferior, superior):

    for valor in range(inferior, superior + 1):
        if eh_primo(valor):
            print(valor)
        else:
            continue


def eh_primo(n):
    qtd = 0

    for i in range(1, n + 1):
        if n % i == 0:
            qtd += 1
            
    if qtd == 2:
        return True
    else:
        return False


main()
def main():
    n = int(input('Digite um número: '))

    print(media(n))


def media(n):
    soma = 0
    for i in range(1, n + 1):
        valor = float(input(f'Valor {i}: '))
        soma += valor
    media_valor = soma / n
    return media_valor


main()
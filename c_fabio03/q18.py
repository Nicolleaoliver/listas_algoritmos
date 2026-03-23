def main():
    n = int(input('Digite um valor para N: '))

    soma_fracoes(n)

def soma_fracoes(n):
    s = 0
    novo_denominador = n
    novo_numerador = 0
    for i in range(1, n + 1):
        novo_numerador += 1
        s += novo_numerador / novo_denominador
        novo_denominador -= 1
    print(f'{s:.2f}')


main()

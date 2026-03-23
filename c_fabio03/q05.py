def main():
    n = int(input('Digite um número fatorial: '))

    fatorial(n)




def fatorial(n):
    resultado = n

    for i in range(n, 1, -1):
        resultado *= i - 1
    print(resultado)


main()
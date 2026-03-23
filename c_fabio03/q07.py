def main():
    n = int(input('Digite um número: '))

    soma(n)


def soma(n):
    resultado = 1
    for i in range(1, n):
        resultado += (i + 1)
    print(resultado)
    #preciso somar o numero atual pelo (i) pelo próximo (i+1), ex: i = 1 i + 2 = 3
    #3 + (2 + 1) = 6
    #6 + (3 + 1) = 10
    #10 + (4 + 1) = 15
main()
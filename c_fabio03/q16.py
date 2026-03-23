def main():
    n = int(input('Digite um número: '))

    fibonacci(n)


def fibonacci(n):
    presente = 1
    passado = 0
    soma = 0

    for i in range(0, n + 1):
        print(soma)
        passado = presente
        presente = soma
        soma = presente + passado
        


main()
def main():
    n = int(input('Digite um número: '))

    obter_maior_quadrado(n)


def obter_maior_quadrado(n):
    for i in range(n, 1, -1):
        raiz = i ** 0.5
        if raiz % 1 == 0:
            print(i)
            break


main()


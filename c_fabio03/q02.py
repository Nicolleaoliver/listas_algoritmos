def main():
    n = int(input('Digite um número: '))

    pares(n)


def pares(n):
    for i in range(2, n + 1, 2):
        print(i)

main()
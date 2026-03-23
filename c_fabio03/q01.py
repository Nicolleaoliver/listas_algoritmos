def main():
    n = int(input('Digite um número: '))

    ler_ate_n(n)



def ler_ate_n(n):
    for i in range(1, n + 1):
        print(i)


main()
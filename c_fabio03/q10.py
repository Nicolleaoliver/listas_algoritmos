def main():
    inferior = int(input('Limite inferior: '))
    superior =  int(input('Limite superior: '))

    impares(inferior, superior)


def impares(inferior, superior):
    for i in range(inferior, superior + 1):
        if i % 2 != 0:
            print(i)


main()
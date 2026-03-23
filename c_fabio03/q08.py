def main():
    n = int(input('Digite um número: '))
    inferior = int(input('Limite inferior: '))
    superior =  int(input('Limite superior: '))

    multiplos(n, inferior, superior)


def multiplos(n, inferior, superior):
    for i in range(inferior, superior + 1):
        if i % n == 0:      
            print(i)


main()
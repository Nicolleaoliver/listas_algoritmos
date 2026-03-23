def main():
    n = int(input('Qual tabuada você quer saber? '))

    tabuada(n)


def tabuada(n):
    for i in range(0, 11):
        multiplicacao = i * n
        print(f'{n} x {i} = {multiplicacao}')



main()
def main():
    n = int(input('Digite um número: '))
    
    sequencia(n)

def sequencia(n):
    #somar 1 a cada incremento
    atual = 1
    incremento = 2
    for i in range(0, n + 1):
        print(atual)
        atual = atual + incremento
        incremento += 1
        


main()
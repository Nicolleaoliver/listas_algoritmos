def main():
    n = int(input('Digite um valor para N: '))

    soma_fracoes(n)


def soma_fracoes(n):
    s = 0
    denominador = n
    num_par = n - 1  # Numerador que começa em 4 (se n=5) e vai descendo
    
    for i in range(1, n + 1):
        if i % 2 != 0:
            # Termos ímpares (1, 3, 5...): Somam e o numerador é o próprio i
            s += i / denominador
        else:
            # Termos pares (2, 4...): Subtraem e o numerador vem da nossa variável
            s -= num_par / denominador
            num_par -= 1  # Diminui o numerador par para a próxima vez
            
        denominador -= 1  # O denominador sempre diminui, independente de ser par ou ímpar

    print(f'S = {s:.2f}')



main()

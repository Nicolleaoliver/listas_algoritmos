def main():
    n = int(input('Quantos habitantes? '))

    media_populacao(n)


def media_populacao(n):
    soma_salario = 0
    qtd_ate_mil = 0

    for i in range(1, n + 1):
        print(f'Habitante {i}: ')
        salario = float(input('Salário: '))
        n_filhos = int(input('Número de filhos: '))

        soma_salario += salario
        n_filhos += n_filhos
        if salario <= 1000:
            qtd_ate_mil += 1

    media_salarial = soma_salario / n
    media_filhos = n_filhos / n
    percentual = (qtd_ate_mil / n) * 100

    print(f'>> Média salarial da população: {media_salarial:.2f}')
    print(f'>> Média de número de filhos: {media_filhos:.2f}')
    print(f'>> Percentual de pessoas que recebem até R$ 1000,00: {percentual:.0f}%')

main()
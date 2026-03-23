def main():
    qtd = int(input('Qual a quantidade de valores: '))

    obter_maior(qtd)


def obter_maior(qtd):
    maior_atual = 0
    for i in range(1, qtd + 1):
        n = float(input(f'Valor {i}: '))
        
        if n > maior_atual:
            maior_atual = n
        else:
            maior_atual = maior_atual
    return maior_atual
        


main()
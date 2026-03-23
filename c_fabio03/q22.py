def main():
    qtd_fichas = int(input('Quantas fichas? '))

    peso(qtd_fichas)

def peso(n):
    maior = 0
    menor = 0
    id_maior = 0
    id_menor = 0

    for i in range(1, n + 1):
        num_id = int(input(f'Boi {i}\nNúmero de Identificação: '))
        nome = input('Nome: ')
        peso_atual = float(input('Peso: '))

        if i == 1:
            maior = peso_atual
            id_maior = num_id
            menor = peso_atual
            id_menor = num_id
        else:
            if peso_atual > maior:
                maior = peso_atual
                id_maior = num_id
            if peso_atual < maior:
                menor = peso_atual
                id_menor = num_id
    print(f'Boi mais pesado:\nNúmero de identificação: {id_maior}, peso: {maior}\nBoi mais magro:\nNúmero de identificação: {id_menor}. peso: {menor}')

main()
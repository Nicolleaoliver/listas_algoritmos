#entrada
#notas de 50, 10, 5 e 1 - para saque de 87, 1 nota de 50, 3 notas de 10, 1 nota de 5 e 2 notas de 1
quantia = int(input('Qual a quantia de saque? '))

#processamento
notas_50 = quantia // 50
resto = quantia % 50
notas_10 = resto // 10
notas_5 = (resto % 10) // 5
notas_1 = (resto % 10) % 5

#saída
print(f'Para sacar {quantia} reais utiliza-se: {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} de 5 e {notas_1} notas de 1')

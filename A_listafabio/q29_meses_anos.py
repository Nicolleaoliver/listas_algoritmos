#entrada de dados
meses = int(input('Meses: '))

#processamento
anos = meses // 12
meses_restantes = meses % 12

#saída de dados
print(f'{meses} meses equivale a {anos} anos e {meses_restantes} meses')
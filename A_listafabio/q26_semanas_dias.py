#entrada de dados
dias = int(input('Valor inteiro em dias: '))

#processamento
semanas = dias // 7
dias_restantes = dias % 7

#saída
print(f'{dias} dias equivale a {semanas} semana e {dias_restantes} dias')
#entrada de dados
metros = float(input('Digite um valor em metros: '))

#processamento
valor_km = metros // 1000
valor_m = metros % 1000

#saída
print(f'{metros} metros equivale a {valor_km} quilômetros e {valor_m} metros ')
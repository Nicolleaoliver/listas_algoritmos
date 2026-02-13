#entrada de dados
numero = int(input('Número com 3 dígitos: '))

#processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = (unidade * 100) + (dezena * 10) + centena
diferenca = numero - inverso

#532 / 235 - 2 * 100 = 200 + (dezena * 10 = 30) + centena
#saída de dados
print(f'{numero} - {inverso} = {diferenca}')
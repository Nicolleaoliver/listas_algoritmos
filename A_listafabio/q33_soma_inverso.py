#entrada
numero = int(input('Número com 3 dígitos: '))

#processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = (unidade * 100) + (dezena * 10) + centena
soma = numero + inverso

#saída
print(f'{numero} + {inverso} = {soma}')
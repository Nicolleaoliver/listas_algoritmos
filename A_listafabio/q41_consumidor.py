#entrada
custo_fabrica = float(input('Custo de fábrica do carro: '))

#processamento
porcentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_consumidor = custo_fabrica + porcentagem_distribuidor + impostos

#saída
print(f'O custo do carro ao consumidor é de {custo_consumidor} reais')
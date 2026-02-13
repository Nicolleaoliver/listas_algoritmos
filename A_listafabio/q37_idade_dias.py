#entrada
idade_dias = int(input('Sua idade em dias: '))

#processamento
idade_em_anos = idade_dias // 365
resto_idade = idade_dias % 365
idade_em_meses = resto_idade // 30
idade_em_dias = resto_idade % 30

#saída
print(f'{idade_dias} dias correspondem a idade de {idade_em_anos} anos, {idade_em_meses} meses e {idade_em_dias} dias')
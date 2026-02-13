#entrada
idade_anos = int(input('Sua idade em anos: '))
idade_meses = int(input('Sua idade em meses: '))
idade_dias = int(input('Sua idade de em dia: '))

#processamento
idade_total_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

#processamento
print(f'A sua idade total corresponde a {idade_total_dias} dias')
#entrada de dados
valor_em_minutos = int(input('Insira um valor em minutos: '))

#processamento
valor_em_horas = valor_em_minutos//60
resto = valor_em_minutos % 60

#saída de dados
print(f'O valor em minutos {valor_em_minutos} corresponde a {valor_em_horas} horas e {resto} minutos')
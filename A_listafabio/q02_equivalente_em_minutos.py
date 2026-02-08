#entrada de dados
valor_em_horas = int(input('Insira um valor em horas: '))
valor_em_minutos = int(input('Insira agora um valor em minutos: '))

#processamento
equivalente_em_minutos = (valor_em_horas * 60) + valor_em_minutos

#saída de dados
print(f'O valor de {valor_em_horas} horas e {valor_em_minutos} minutos equivale a {equivalente_em_minutos} minutos')


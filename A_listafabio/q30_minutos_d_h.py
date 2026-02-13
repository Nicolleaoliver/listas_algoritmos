#entrada de dados
minutos = int(input('Minutos: '))

#processamento
dias = minutos // 1440
resto = minutos % 1440
horas = resto // 60
minutos_restantes = resto % 60

#saída de dados
print(f'{minutos} minutos equivale a {dias} dias, {horas} horas e {minutos_restantes} minutos')
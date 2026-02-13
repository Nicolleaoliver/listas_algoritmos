#entrada de dados
horas = int(input('Horas: '))

#processamento
semanas = horas // 168
resto = horas % 168
dias = resto // 24
horas_restantes = resto % 24

#saída
print(f'{horas} horas equivale a {semanas} semanas, {dias} dias e {horas_restantes} horas')
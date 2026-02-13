#entrada de dados
segundos = int(input('Segundos: '))

#processamento
horas = segundos // 3600
resto = (segundos % 3600)   
minutos = resto // 60   
segundos_restantes = resto % 60  
4450

#saída de dados 
print(f'{segundos} segundos equivale a {horas} horas, {minutos} minutos e {segundos_restantes} segundos')
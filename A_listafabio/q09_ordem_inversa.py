#Se a entrada for 1 input
#entrada de dados
numero_um = int(input('Número um número com dois dígitos: '))

#processamento
#faz o calculo de cada casa numerica
dezena = numero_um // 10
unidade = (numero_um % 10) 

#saída de dados
print(f'Seu número na ordem inversa: {unidade}{dezena}')



#Se a entrada for mais de um input
#entrada de dados
numero_um = input('Número 1: ')
numero_dois = input('Número 2: ')

#processamento
ordem_inversa = numero_dois + numero_um #concatena as strings

#saída de dados
print(f'A ordem inversa de seus números é {ordem_inversa}')

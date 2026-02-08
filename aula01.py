#Entrada de dados
#real, int, float, str
limite_superior = int(input('Limite Superior: '))
limite_inferior = int(input('Limite Inferior: '))

soma_dos_pares = (limite_superior + limite_inferior) #15
quantidade_de_numeros = (limite_superior - limite_inferior) + 1 #quantidade de números no intervalo

somatorio = (soma_dos_pares * quantidade_de_numeros) / 2

print(f'O somatório de {limite_inferior} a {limite_superior} é: {somatorio}')


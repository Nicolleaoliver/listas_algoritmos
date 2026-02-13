#entrada
numero = int(input('Número com 4 dígitos: '))

#processamento
milhar = numero // 1000
resto = numero % 1000
centena = resto // 100
dezena = (resto % 100) // 10
unidade = (resto % 100) % 10

soma_elementos = milhar + centena + dezena + unidade

#saída 
print(f'A soma dos elementos de {numero} é igual a {soma_elementos}')
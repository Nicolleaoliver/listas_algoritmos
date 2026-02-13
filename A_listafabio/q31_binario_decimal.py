#entrada de dados
numero = int(input('Digite um número com 4 dígitos binários (0 ou 1): '))

#processamento
milhar = numero // 1000
resto = numero % 1000 #101, no exemplo do número 1101
centena = resto // 100
dezena = (resto % 100) // 10
unidade = resto % 10

conversao = (milhar * (2 ** 3)) + (centena * (2 ** 2)) + (dezena * (2 ** 1)) + (unidade * (2 ** 0))

#saída de dados
print(f'{numero} em binario é {conversao} em decimal')


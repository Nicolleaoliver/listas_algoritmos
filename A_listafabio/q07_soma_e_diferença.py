#entrada de dados
numero = int(input('Insira um número de 3 dígitos: '))

#processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

#somando os dois primeiros
soma_dois_primeiros = centena + dezena
diferenca_dois_ultimos = dezena - unidade

#saída de dados
print(f'A soma dos dois primeiros números é {soma_dois_primeiros} e a diferença entre os dois últimos é {diferenca_dois_ultimos}')


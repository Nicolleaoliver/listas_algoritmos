#entrada de dados
valor_tres_digitos = int(input('Insira um valor de 3 dígitos: '))

#processamento
centena = valor_tres_digitos // 100
dezena = (valor_tres_digitos % 100) // 10
unidade = (valor_tres_digitos % 100) % 10

#saída de dados
print(f'O inverso do número {valor_tres_digitos} é {unidade}{dezena}{centena}')
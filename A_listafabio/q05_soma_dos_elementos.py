#entrada de dados
numero_tres_digitos = int(input('Digite um número com 3 dígitos (CDU): '))

#processamento
numero_centena = numero_tres_digitos//100
numero_dezena = (numero_tres_digitos % 100) // 10
resto_dezena = numero_tres_digitos % 100
numero_unidade = resto_dezena % 10


soma_dos_elementos = numero_centena + numero_dezena + numero_unidade

#saída de dados 
print(f'A soma dos elementos do número {numero_tres_digitos} é igual a {soma_dos_elementos}')

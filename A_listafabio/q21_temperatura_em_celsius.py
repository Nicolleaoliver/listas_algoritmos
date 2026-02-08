#entrada de dados
temperatura_fahrenheit = float(input('Digite uma temperatura em graus Fahrenheit: '))

#processamento
temperatura_celsius = (5 * temperatura_fahrenheit - 160) / 9

#saída de dados
print(f'{temperatura_fahrenheit} graus Fahrenheit equivale a {temperatura_celsius} graus Celsius')
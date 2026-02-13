#entrada
valor_mercadoria = float(input('Valor da mercadoria: '))

#processamento
resto = valor_mercadoria % 3
entrada = (valor_mercadoria // 3) + resto
prestacoes = (valor_mercadoria - entrada) / 2

#saída
print(f'A mercadoria tem a entrada de R${entrada}, e 2 prestações de R${prestacoes}')
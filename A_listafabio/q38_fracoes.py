#entrada
#fração 1
numerador_1 = int(input('Numerador da fração 1: '))
denominador_1 = int(input('Denominador da fração 1: '))

numerador_2 = int(input('Numerador da fração 2: '))
denominador_2 = int(input('Denominador da fração 2: '))

#processamento
mdc = denominador_1 % denominador_2
mmc = (denominador_1 * denominador_2) / mdc
#calcula a soma dos numeradores
calculo_numerador_1 = (mmc / denominador_1) * numerador_1
calculo_numerador_2 = (mmc / denominador_2) * numerador_2
soma_numeradores = calculo_numerador_1 + calculo_numerador_2

#saída
print(f'A soma das frações {numerador_1}/{denominador_1} + {numerador_2}/{denominador_2} é {soma_numeradores}/{mmc}')
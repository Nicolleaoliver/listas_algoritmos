#entrada de dados
nota1 = float(input('Primeira nota: '))
peso1 = float(input('Peso da primeira nota: '))

nota2 = float(input('Segunda nota: '))
peso2 = float(input('Peso da segunda nota: '))

nota3 = float(input('Terceira nota: '))
peso3 = float(input('Peso da terceira nota: '))

#processamento
media_ponderada = (nota1 + nota2 + nota3) / (peso1 + peso2 + peso3)

#saída de dados
print(f'A média das suas notas é {media_ponderada}')
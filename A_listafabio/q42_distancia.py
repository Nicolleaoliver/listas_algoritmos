#entrada
#ponto 1
x1 = float(input('X1: '))
y1 = float(input('Y1: '))

#ponto 2
x2 = float(input('X2: '))
y2 = float(input('Y2: '))

#processamento
diferenca_x2_x1 = (x2 - x1) ** 2
diferenca_y2_y1 = (y2 - y1) ** 2

d = (diferenca_x2_x1 + diferenca_y2_y1) ** 0.5

#saída
print(f'A distância entre os pontos 1 e 2 é {d}')
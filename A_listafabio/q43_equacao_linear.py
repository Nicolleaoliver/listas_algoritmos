#entrada
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))
d = float(input('D: '))
e = float(input('E: '))
f = float(input('F: '))

#processamento
denominador =  (a* e) - (b * d)
x = ((c * e) - (b * f)) / denominador
y = ((a * f) - (c * d)) / denominador

#saída
print(f'O valor de x é {x} e o valor de y é {y}')


def soma_fracoes():
    numerador = 1
    s = 0
    for i in range(1, 51):
        s += numerador / i
        numerador += 2
    print(s)

soma_fracoes()
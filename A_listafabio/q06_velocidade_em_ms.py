#entrada de dados
velocidade_em_kmh = float(input('Insira um valor em kmh: '))

#processamento
velocidade_em_ms = velocidade_em_kmh / 3.6

#saída de dados
print(f'{velocidade_em_kmh} kmh equivale a {velocidade_em_ms} ms')
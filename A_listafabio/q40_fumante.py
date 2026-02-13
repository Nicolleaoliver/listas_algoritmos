#entrada
anos_fumando = int(input('Há quantos anos você fuma: '))
quant_dia = int(input('Quantos cigarros você fuma por dia: '))
preco_carteira = int(input('Quanto custa a carteira de cigarros? '))

#uma carteira tem 20 cigarros
#processamento
quant_carteiras_dia = (quant_dia + 19) // 20 #quantas carteiras inteiras no dia
preco_dia = quant_carteiras_dia * preco_carteira #valor gasto num dia com base na quantidade de carteiras por dia
anos_em_dias = anos_fumando * 365
preco_total_anos = anos_em_dias * preco_dia

#saída
print(f'O valor gasto com carteiras de cigarro é {preco_total_anos} reais')
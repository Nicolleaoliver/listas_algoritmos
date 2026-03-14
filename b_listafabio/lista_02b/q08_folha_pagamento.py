from utils_io import escrever, obter_numero_real
from utils import calcular_pagamento


def main():
    valor_hora = obter_numero_real('> Valor da hora trabalhada: ')
    quant_horas = obter_numero_real('> Quantidade de horas trabalhadas mensais: ')

    salario_bruto, ir_percentual, valor_ir, inss, fgts, total_desconto, salario_liquido = calcular_pagamento(valor_hora, quant_horas)

    escrever(f'Salário bruto: ({valor_hora}*{quant_horas})          :R${salario_bruto}\n(-) IR ({ir_percentual}):          :R${valor_ir}\n(-) INSS (10%):          :R${inss}\nFGTS (11%):          :R${fgts}\nTotal de descontos:          :R${total_desconto}\nSalário Líquido:          :R${salario_liquido}')



main()
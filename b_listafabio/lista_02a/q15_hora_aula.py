from utils_io import escrever, obter_numero_real
from utils import calcular_horas_aula

def main():
    escrever('Vamos calcular o salário de dois professores')
    nome1 = input('Nome do professor 1: ')
    nome2 = input('Nome do professor 2: ')

    escrever(f'>> Professor {nome1}<<')
    valor_hora_prof1 = obter_numero_real('Valor da hora aula: ')
    quant_horas_prof1 = obter_numero_real('Quantidade de horas trabalhadas : ')

    escrever(f'>> Professor {nome2}<<')
    valor_hora_prof2 = obter_numero_real('Valor da hora aula: ')
    quant_horas_prof2 = obter_numero_real('Quantidade de horas trabalhadas: ')

    salario1, salario2 = calcular_horas_aula(valor_hora_prof1, quant_horas_prof1, valor_hora_prof2, quant_horas_prof2)
    escrever(f'Salário professor {nome1}: {salario1}\nSalário professor {nome2}: {salario2}')


main()
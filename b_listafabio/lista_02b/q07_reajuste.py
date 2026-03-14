from utils_io import escrever, obter_numero_real
from utils import reajuste


def main():
    escrever('>> Haverá um reajuste no salário dos colaboradores. Informe o valor do seu salário para saber qual será o seu reajuste <<')
    salario = obter_numero_real('Salário: ')

    percentual, valor_aumento, novo_salario = reajuste(salario)

    escrever(f'> Salário anterior ao reajuste: {salario}\n> Percentual de aumento aplicado: {percentual}\n> Valor do aumento: {valor_aumento}\n> Salário após o aumento: {novo_salario}')

main()
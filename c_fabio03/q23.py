def main():
    qtd_func = int(input('Quantos funcionários? '))

    salario_liquido(qtd_func)


def salario_liquido(qtd_func):
    desconto_inss = 0
    desconto_ir = 0
    salario_bruto = 0
    salario_liquido = 0
    valor_hora = 12
    valor_dependente = 40
    total_dependentes = 0

    for i in range(1, qtd_func + 1):
        print(f'Funcionário {i}')
        codigo_func = int(input('Código funcionário: '))
        qtd_horas = int(input('Quantidade de horas trabalhadas: '))
        n_dependentes = int(input('Quantos dependentes? '))

        total_dependentes = n_dependentes * valor_dependente
        salario_bruto = (valor_hora * qtd_horas) + total_dependentes
        desconto_inss = salario_bruto * 0.085
        desconto_ir = salario_bruto * 0.05
        total_desconto = desconto_inss + desconto_ir
        
        salario_liquido = salario_bruto - total_desconto
        print(f'Desconto INSS: {desconto_inss:.2f}\nDesconto IR: {desconto_ir:.2f}\nSalário Liquido: {salario_liquido:.2f}')


main()
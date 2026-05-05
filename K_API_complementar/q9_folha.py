from utils import obter_int, obter_real

def main():
    n = obter_int('Quantidade de funcionários: ')
    total_folha, maior, menor = computar_salarios(n)
    print(f'''Maior salário: {maior:.2f}
Menor salário: {menor:.2f}
Total gasto com a folha: {total_folha:.2f}''')

def computar_salarios(n):
    maior = 0
    menor = 0
    total_folha = 0
    contador = 0

    for i in range(1, n + 1):
        print(f'===== Funcionário {i} =====')
        nome = input('Nome Funcionário: ')
        salario_bruto = obter_real('Salário bruto: ')
        qtd_horas = obter_int('Quantidade de horas trabalhadas: ')

        qtd_horas_extras = qtd_horas - 220
        valor_h = salario_bruto / 220
        valor_h_extra = valor_h * 1.5
        total_h_extra = valor_h_extra * qtd_horas_extras
        valor_inss = salario_bruto * 0.11
        if salario_bruto > 2000:
            salario_liquido = (salario_bruto + total_h_extra) - valor_inss - 150
        else:
            salario_liquido = (salario_bruto + total_h_extra) - valor_inss
        print(f'''--- EXTRATO {nome} ---
Salário bruto:     R${salario_bruto:.2f}
Horas Extras:     R${total_h_extra:.2f}
INSS:     R${valor_inss:.2f}
Vale Refeição:     R$150,00
Salário Líquido:     R${salario_liquido:.2f}
---''')
        total_folha += salario_liquido
        if contador == 0:
            maior = salario_liquido
            menor = salario_liquido
        else:
            if salario_liquido > maior:
                maior = salario_liquido
            if salario_liquido < menor:
                menor = salario_liquido
        contador += 1
    return total_folha, maior, menor
        

main()
from utils_io import obter_numero_real

def verificar_iguais(numero1, numero2, numero3):
    if numero1 == numero2 == numero3:
        return 'Há três números iguais'
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return 'Há dois números iguais'
    else:
        return 'Todos são diferentes'


def obter_maior_e_menor(numero1, numero2):
    if numero1 > numero2:
        return f'Menor: {numero2}, maior: {numero1}'
    elif numero2 > numero1:
        return f'Menor: {numero1}, maior: {numero2}'
    else:
        return 'Os dois são iguais'
    

def obter_maior(numero1, numero2, numero3):
    if numero1 == numero2 == numero3:
        return 'Todos são iguais'
    if numero1 > numero2 and numero1 > numero3:
        maior = numero1
        return maior
    elif numero2 > numero1 and numero2 > numero3:
        maior = numero2
        return maior
    elif numero3 > numero1 and numero3 > numero2:
        maior = numero3
        return maior
    

def dezena_unidade(numero):
    dezena = numero // 10
    unidade = numero % 10

    if dezena != unidade:
        return 'O algarismo da dezena é diferente da unidade'
    else:
        return 'O algarismo da dezena e da unidade são iguais'
    

def ordem_crescente(numero1, numero2, numero3):
    if numero1 == numero2 == numero3:
        return 'Os três são iguais'
    
    menor, meio, maior = numero1, numero2, numero3
    if menor > meio:
        menor, meio = meio, menor

    if meio > maior:
        meio, maior = maior, meio

    if menor > meio:
        menor, meio = meio, menor

    return menor, meio, maior


def is_triangle_angle(angulo1, angulo2, angulo3):
    if (angulo1 + angulo2 + angulo3) == 180 and angulo1 != 0 and angulo2 != 0 and angulo3 != 0:
        return True
    else:
        return False



def type_triangle_angle(angulo1, angulo2, angulo3):
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return 1
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return 2
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        return 3
    
    
def is_triangle_side(lado1, lado2, lado3):
    if (lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2)) and lado1 != 0 and lado2 != 0 and lado3 != 0:
        return True
    else:
        return False
    
    
def type_triangle_side(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'E esse triângulo é equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'E esse triângulo é isósceles'
    elif lado1 != lado2 != lado3:
        return 'E esse triângulo é escaleno'
    

def obter_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    idade = ano_atual - ano_nasc
    if (mes_atual < mes_nasc) or (dia_atual < dia_nasc):
        idade = idade -1
        return idade
    return idade
    
def idade_em_anos_meses_dias(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    idade = ano_atual - ano_nasc

    if (dia_atual == dia_nasc) and (mes_atual == mes_nasc):
        quant_meses = 0
        quant_dias = 0
        return idade, quant_meses, quant_dias
    else:
        if mes_atual < mes_nasc:
            idade -= 1
            quant_meses = mes_atual + (12 - mes_nasc)
            if dia_atual < dia_nasc:
                quant_dias = dia_atual
                return idade, quant_meses, quant_dias
            elif dia_atual > dia_nasc:
                quant_dias = dia_atual
                return idade, quant_meses, quant_dias
        elif mes_atual > mes_nasc:
            quant_meses = mes_atual - mes_nasc
            if dia_atual < dia_nasc:
                quant_dias = dia_atual
                return idade, quant_meses, quant_dias
            elif dia_atual > dia_nasc:
                quant_dias = dia_atual
                return idade, quant_meses, quant_dias
        
    
def eh_primo(numero):
    if numero == 0:
        return 'Não é primo'
    else:
        if numero % (numero ** 0.5) != 0:
            if numero > 100:
                print('Só insira números até o 100')
            else:
                primo = print('É primo')
            return primo
        
def verificar_data(dia, mes, ano):
    if mes > 12 or dia > 31 or ano > 2026 or (mes == 2 and dia >= 30) or dia < 1:
        return 'Data inválida'
    else:
        return 'Data válida'

def obter_opcao(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    else:
        return 'Opcao é inválida'
    

def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

def higher_lower(num1, num2, num3, num4, num5):
    maior = num1
    menor = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5

    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5

    return maior, menor
        

def media_maior(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5) / 5
    
    maior = num1
    
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3
    if num4 > maior:
        maior = num4
    if num5 > maior:
        maior = num5

    return media, maior 


def calcular_horas_aula(valor_hora1, horas1, valor_hora2, horas2):
    salario1 = valor_hora1 * horas1
    salario2 = valor_hora2 * horas2
    return salario1, salario2


def media_nota(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media > 7:
        return 'Aprovado'
    elif media < 7:
        nota_final = obter_numero_real('Nota final: ')
        media_final = (nota1 + nota_final) / 2
        if media_final >= 5:
            return 'Aprovado'
        else:
            return 'Reprovado'
        

def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def verificar_restos(num1, num2):
    if num1 % num2 == 1:
        soma = num1 + num2
        somar = soma + 1
        return somar
    elif num1 % num2 == 2:
        resultado = ''
        if eh_par(num1):
            resultado += f'{num1} é par e '
        else:
            resultado += f'{num1} é ímpar e'
        
        if eh_par(num2):
            resultado += f'{num2} é par'
        else:
            resultado += f'{num2} é ímpar'
        return resultado
    elif num1 % num2 == 3:
        multiply = soma * num1
        return multiply
    elif num1 % num2 == 4:
        if num2 != 0:
            division = soma / num2
            return division
        else:
            return 'Não existe divisão por zero'
    else:
        quadrado1 = num1 ** 0.5
        quadrado2 = num2 ** 0.5
        return f'Quadrado de {num1}: {quadrado1}; quadrado de {num2}: {quadrado2}'
    


def operacoes(valor1, valor2, operacao):
    soma = 1
    subtracao = 2
    multiplicacao = 3
    divisao = 4

    if operacao == soma:
        soma = valor1 + valor2
        return soma
    elif operacao == subtracao:
        subtracao = valor1 - valor2
        return subtracao
    elif operacao == multiplicacao:
        multiplicacao = valor1 * valor2
        return multiplicacao
    elif operacao == divisao:
        divisao = valor1 / valor2
        return    
    

def quadrante(angulo):
    if angulo <= 90:
        return 'quadrante 1'
    elif angulo <= 180:
        return 'quadrante 2'
    elif angulo <= 270:
        return 'quadrante 3'
    elif angulo <= 360:
        return 'quadrante 4'
    else:
        return 'valor fora do intervalo esperado'


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def obter_classificacao_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obesidade Grau I'
    elif imc < 40:
        return 'Obesidade Grau II'
    elif imc > 40:
        return 'Obesidade Grau III'


def arredondar(num):
    inteiro = int(num)
    subtracao = num - inteiro
    if subtracao <= 4:
        num = inteiro
        return num
    elif subtracao >= 5:
        num = inteiro + 1
        return num
    

def obter_duracao_jogo(hora_inicio, min_inicio, hora_final, min_final):
    total_horas = hora_final - hora_inicio
    total_min = min_final - min_inicio

    if min_final < min_inicio:
        total_min += 60
        total_horas -= 1
    
    if hora_final < hora_inicio:
        total_horas += 24
    return total_horas, total_min


def data_recente(dia1, mes1, ano1, dia2, mes2, ano2):
    ano_recente = ano1 
    mes_recente = mes1 
    dia_recente = dia1

    if ano2 > ano_recente:
        ano_recente = ano2
    if mes2 > mes_recente:
        mes_recente = mes2
    if dia2 > dia_recente:
        dia_recente = dia2
    return ano_recente, mes_recente, dia_recente


def obter_delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if a != 0:
        if delta > 0:
            mensagem = 'A equação possui duas raízes reais e diferentes.'
            return delta, mensagem
        if delta == 0:
            mensagem = 'A equação possui uma única raiz real (ou duas raízes iguais).'
            return delta, mensagem
        if delta < 0:
            mensagem = 'A equação não possui raízes reais (apenas complexas).'
            return delta, mensagem
    else:
        return 'O coeficiente a não pode ser 0'
    

def obter_raizes(a, b, delta):
    if delta < 0:
        return None, None
    
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)
    return x1, x2


def validar_senha(senha):
    senha_correta = 1234
    if senha == senha_correta:
        return 'Acesso permitido'
    else:
        return 'Acesso negado'
    

def cartesiano(x1, y1, x2, y2):
    base = x2 - x1
    altura = y2 - y1

    area = base * altura
    if area < 0:
        area = area * -1
        return area
    return area


def is_quadrado_perfeito(num):
    raiz = num ** 0.5
    milhar= num // 1000
    centena = (num % 1000) // 100
    resto = num % 1000
    dezena = resto % 100
    #unidade = (resto % 100) % 10

    dezena1 = (milhar * 10) + centena
    soma = dezena1 + dezena
    codigo = 0
    if soma == raiz:
        codigo = 1
        return codigo, dezena, dezena1
    return codigo, dezena, dezena1


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def calcular_nota_sisu(nota1, peso1, nota2, peso2, nota_redacao, peso3, bonus_regional):
    media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota_redacao * peso3)) / (peso1 + peso2 + peso3)
    calc_bonus = (bonus_regional * 0.01)
    valor_acrescido = media_ponderada * calc_bonus
    soma_media_bonus = media_ponderada + valor_acrescido
    return soma_media_bonus


def is_positive_negative(num):
    codigo = 0
    if num >= 0:
        codigo = 1
        return codigo
    return codigo


def fem_masc(resposta):
    codigo = 0
    if resposta == 'F':
        codigo = 1
        return codigo
    elif resposta == 'M':
        codigo == 2
        return codigo
    return codigo

def is_vogal(letra):
    return letra in 'aeiou'

def situacao_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media == 10:
        return 'Aprovado com Distinção'
    elif media > 7:
        return 'Aprovado'
    elif media < 7:
        return 'Reprovado'
    

def turno(texto):
    if texto == 'M':
        return 'Bom Dia!'
    if texto == 'V':
        return 'Boa Tarde!'
    if texto == 'N':
        return 'Boa Noite!'
    if texto not in 'MVN':
        return 'Valor Inválido!'
    

def reajuste(salario):
    vinte_porcento = salario * 0.20
    quinze_porcento = salario * 0.15
    dez_porcento = salario * 0.10
    cinco_porcento = salario * 0.05

    if salario <= 280:
        percentual = '20%'
        valor_aumento = vinte_porcento
        novo_salario = salario + vinte_porcento
    elif salario <= 700:
        percentual = '15%'
        valor_aumento = quinze_porcento
        novo_salario = salario + quinze_porcento
    elif salario <= 1500:
        percentual = '10%'
        valor_aumento = dez_porcento
        novo_salario = salario + dez_porcento
    elif salario > 1500:
        percentual = '5%'
        valor_aumento = cinco_porcento
        novo_salario = salario + cinco_porcento

    return percentual, valor_aumento, novo_salario


def calcular_pagamento(valor_hora, quant_horas):
    salario_bruto = valor_hora * quant_horas
    #sindicato = salario_bruto * 0.03
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11

    salario_parcial = (salario_bruto - inss)

    if salario_bruto <= 900:
        ir_percentual = '0%'
        valor_ir = 0
        total_desconto = valor_ir + inss
        salario_liquido = salario_parcial - ir_percentual
    elif salario_bruto <= 1500:
        ir_percentual = '5%'
        valor_ir = salario_bruto * 0.05
        total_desconto = valor_ir + inss
        salario_liquido = salario_parcial - valor_ir
    elif salario_bruto <= 2500:
        ir_percentual = '10%'
        valor_ir = salario_bruto * 0.10
        total_desconto = valor_ir + inss
        salario_liquido = salario_parcial - valor_ir
    elif salario_bruto > 2500:
        ir_percentual = '20%'
        valor_ir = salario_bruto * 0.20
        total_desconto = valor_ir + inss
        salario_liquido = salario_parcial - valor_ir
    
    return salario_bruto, ir_percentual, valor_ir, inss, fgts, total_desconto, salario_liquido


def semana(dia):
    if dia == 1:
        return 'Domingo'
    elif dia == 2:
        return 'Segunda'
    elif dia == 3:
        return 'Terça'
    elif dia == 4:
        return 'Quarta'
    elif dia == 5:
        return 'Quinta'
    elif dia == 6:
        return 'Sexta'
    elif dia == 7:
        return 'Sábado'
    else:
        return 'Valor inválido'
    
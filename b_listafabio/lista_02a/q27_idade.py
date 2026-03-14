from utils_io import escrever, obter_numero_inteiro
from utils_idade import idade2

def main():
    escrever('>>> Qual a data atual? <<<')
    dia_atual = obter_numero_inteiro('> Dia: ')
    mes_atual = obter_numero_inteiro('> Mês: ')
    ano_atual = obter_numero_inteiro('> Ano: ')

    escrever('>>> Insira sua data de nascimento <<< ')
    dia_nasc = obter_numero_inteiro('> Dia: ')
    mes_nasc = obter_numero_inteiro('> Mês: ')
    ano_nasc = obter_numero_inteiro('> Ano: ')

    idade_anos, idade_meses, idade_dias = idade2(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)

    escrever(f'Você tem {idade_anos} anos, {idade_meses} meses e {idade_dias} dias')


main()

'''from utils_io import escrever, obter_numero_inteiro
from utils import idade_em_anos_meses_dias

def main():
    escrever('>>> Qual a data atual? <<<')
    dia_atual = obter_numero_inteiro('> Dia: ')
    mes_atual = obter_numero_inteiro('> Mês: ')
    ano_atual = obter_numero_inteiro('> Ano: ')

    escrever('>>> Insira sua data de nascimento <<< ')
    dia_nasc = obter_numero_inteiro('> Dia: ')
    mes_nasc = obter_numero_inteiro('> Mês: ')
    ano_nasc = obter_numero_inteiro('> Ano: ')
    
    idade, quant_meses, quant_dias = idade_em_anos_meses_dias(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)

    escrever(f'Sua idade é {idade} anos {quant_meses} meses e {quant_dias} dias')

main()'''
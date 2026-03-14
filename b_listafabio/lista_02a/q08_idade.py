from utils_io import escrever, obter_numero_inteiro
from utils import obter_idade

def main():
    escrever('Insira a data atual: ')
    dia_atual = obter_numero_inteiro('> Dia: ')
    mes_atual = obter_numero_inteiro('> Mês: ')
    ano_atual = obter_numero_inteiro('> Ano: ')

    escrever('Agora insira sua data de nascimento:')
    dia_nasc = obter_numero_inteiro('> Dia: ')
    mes_nasc = obter_numero_inteiro('> Mês: ')
    ano_nasc = obter_numero_inteiro('> Ano: ')

    escrever(f'Sua idade é {obter_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc)} anos')


main()
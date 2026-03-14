from utils_io import escrever, obter_numero_inteiro
from utils import data_recente

def main():
    dia1 = obter_numero_inteiro('Dia 1: ')
    mes1 = obter_numero_inteiro('Mes 1: ')
    ano1 = obter_numero_inteiro('Ano 1: ')

    dia2 = obter_numero_inteiro('Dia 2: ')
    mes2 = obter_numero_inteiro('Mes 2: ')
    ano2 = obter_numero_inteiro('Ano 2: ')


    ano_recente, mes_reecente, dia_recente = data_recente(dia1, mes1, ano1, dia2, mes2, ano2)
    escrever(f'A data recente é {dia_recente}/{mes_reecente}/{ano_recente}')


main()


   
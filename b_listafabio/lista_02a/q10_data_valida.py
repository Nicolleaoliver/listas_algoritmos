from utils_io import escrever, obter_numero_inteiro
from utils import verificar_data

def main():
    dia = obter_numero_inteiro('Dia: ')
    mes = obter_numero_inteiro('Mês: ')
    ano = obter_numero_inteiro('Ano: ')
    
    data = verificar_data(dia, mes, ano)
    escrever(data)


main()
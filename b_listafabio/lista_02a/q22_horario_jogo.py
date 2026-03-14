from utils_io import escrever, obter_numero_inteiro
from utils import obter_duracao_jogo

def main():
    hora_inicio = obter_numero_inteiro('Hora início: ')
    min_inicio = obter_numero_inteiro('Minutos início: ')

    hora_final = obter_numero_inteiro('Hora final: ')
    min_final = obter_numero_inteiro('Minutos final: ')

    total_horas, total_min = obter_duracao_jogo(hora_inicio, min_inicio, hora_final, min_final)
    escrever(f'O jogo durou {total_horas} horas e {total_min} minutos')


main()


   
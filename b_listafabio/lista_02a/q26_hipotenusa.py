from utils_io import escrever, obter_numero_real
from utils import is_triangle_side, obter_maior

def main():
    escrever('>>>Insira valores de 3 lados de um triângulo<<<')

    lado1 = obter_numero_real('Lado 1: ')
    lado2 = obter_numero_real('Lado 2: ')
    lado3 = obter_numero_real('Lado 3: ')

    maior = obter_maior(lado1, lado2, lado3)

    if is_triangle_side(lado1, lado2, lado3):
        if maior == lado1:
            escrever(f'O lado {lado1} é a hipotenusa e os lados {lado2} e {lado3} são os catetos')
        elif maior == lado2:
            escrever(f'O lado {lado2} é a hipotenusa e os lados {lado1} e {lado3} são os catetos')
        elif maior == lado3:
            escrever(f'O lado {lado3} é a hipotenusa e os lados {lado1} e {lado2} são os catetos')
    else:
        escrever('Esses lados não formam um triângulo')


    
main()
from utils_io import escrever, obter_numero_real
from utils import is_triangle_side, type_triangle_side


def main():
    escrever('Informe 3 lados e verificarei se eles formam um triângulo')
    
    lado1 = obter_numero_real('> Lado 1: ')
    lado2 = obter_numero_real('> Lado 2: ')
    lado3 = obter_numero_real('> Lado 3: ')
    
    if is_triangle_side(lado1, lado2, lado3):
        escrever(f'Esses lados formam um triângulo. {type_triangle_side(lado1, lado2, lado3)}')
    else:
        if lado1 == 0 or lado2 == 0 or lado3 == 0:
            escrever('Não existe triângulo com lado 0')
        else:
            escrever('Esses lados não formam um triângulo')
        

main()
    
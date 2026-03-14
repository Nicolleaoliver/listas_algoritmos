from utils_io import obter_numero_real, escrever
from utils import is_triangle_angle, type_triangle_angle


def main():
    escrever('Informe três angulos e direi se eles formam um triangulo e qual o tipo dele:')
    angulo1 = obter_numero_real('> angulo 1: ')
    angulo2 = obter_numero_real('> angulo 2: ')
    angulo3 = obter_numero_real('> angulo 3: ')
    
    
    tipo = type_triangle_angle(angulo1, angulo2, angulo3)

    if is_triangle_angle(angulo1, angulo2, angulo3):
        if tipo == 1:
            escrever(f'Esses angulos formam um triângulo, do tipo acutângulo')
        elif tipo == 2:
            escrever(f'Esses angulos formam um triângulo, do tipo retângulo')
        elif tipo == 3:
            escrever(f'Esses angulos formam um triângulo, do tipo obtusângulo')
    else:
        if angulo1 == 0 or angulo2 == 0 or angulo3 == 0:
            escrever('Não existe triângulo com angulo 0')
        else:
            escrever(f'Esses ângulos não formam um triângulo')
        

main()
        


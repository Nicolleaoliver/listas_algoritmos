from utils_io import obter_numero_real
from utils import quadrante

def main():
    angulo = obter_numero_real('Insira um ângulo: ')

    print(quadrante(angulo))



main()
from utils_io import escrever, obter_numero_real
from utils import calcular_imc, obter_classificacao_imc

def main():
    escrever('Vamos calcular seu IMC!')
    peso = obter_numero_real('Peso: ')
    altura = obter_numero_real('Altura: ')

    imc = calcular_imc(peso, altura)
    classificacao = obter_classificacao_imc(imc)

    escrever(f'Seu IMC é {imc:1f} ({classificacao})')

main()
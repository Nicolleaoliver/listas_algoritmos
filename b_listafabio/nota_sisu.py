from utils import calcular_nota_sisu


def main():
    nota_humanas = float(input('Nota na área de Humanas: '))
    peso_humanas = float(input('Peso (1 a 3): '))
    nota_exatas = float(input('Nota da área de exatas: '))
    peso_exatas = float(input('Peso (1 a 3): '))
    nota_redação = float(input('Nota da redação: '))
    peso3 = float(input('Peso (1 a 3): '))

    bonus_regional = float(input('Qual o bonus percenetual para a sua região? '))

    nota_final_sisu = calcular_nota_sisu(nota_humanas, peso_humanas, nota_exatas, peso_exatas, nota_redação, peso3, bonus_regional)

    print(f'Sua nota final no SISU é de {nota_final_sisu}')


main()
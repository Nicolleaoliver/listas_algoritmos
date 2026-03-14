from utils import calcular_imc 

def main():
    num1 = float(input('Peso: '))
    num2 = float(input('Altura: '))
    resultado = calcular_imc(num1, num2) 
    print(f'O seu imc {resultado}')

main()
from utils_io import escrever, obter_texto
from utils import is_fem_masc

def main():
    resposta = obter_texto('Qual o sexo? (F - feminino, M - masculino)  ')

    codigo = is_fem_masc(resposta)
    if codigo == 1:
        escrever('Feminino')
    elif codigo == 2:
        escrever('Masculino')
    else:
        escrever('Sexo inválido') 

main()
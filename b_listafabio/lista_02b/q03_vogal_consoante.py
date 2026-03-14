from utils_io import escrever, obter_texto
from utils import is_vogal

def main():
    letra = obter_texto('Insira uma letra e informarei se é vogal ou consoante: ')

    if is_vogal(letra):
        escrever('É vogal')
    else:
        escrever('É consoante')

main()
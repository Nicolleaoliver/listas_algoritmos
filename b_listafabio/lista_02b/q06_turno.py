from utils_io import escrever, obter_texto
from utils import turno

def main():
    texto = obter_texto('Digite qual o seu turno (M - matutino, V - vespertino, N - noturno): ')

    escrever(turno(texto))


main()
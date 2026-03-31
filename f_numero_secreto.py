import random

def numero_secreto():
    num_sorteado = random.randint(1, 100)
    num = int(input('Tentativa 1: ')) 

    pontuacao = 100
    contador = 0
    num_tentativa = 1

    while contador < 10:
        if num != num_sorteado:
            contador += 1
            pontuacao -= 10
            num_tentativa += 1
            print('Errou!')
            if num < num_sorteado:
                print('O número sorteado é maior')
            else:
                print('O número sorteado é menor')
            num = int(input(f'Tentativa {num_tentativa}: '))
        else:
            print('Acertou!')
            print(f'Pontuação: {pontuacao}')
            break
    else:
        print('Perdeu!')


numero_secreto()
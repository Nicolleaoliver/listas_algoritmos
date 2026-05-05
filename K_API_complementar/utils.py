def obter_int(instrucoes="Digite um número inteiro: "):
    while True:
        try:
            n = int(input(instrucoes))
            return n
        except ValueError:
            print('Valor inválido, digite novamente!')
            continue


def faixa_menu_inicial(instrucoes="Digite um número numa faixa: "):
    while True:
        n = int(input(instrucoes))
        if n != 6 and n != 7 and n != -1:
            print('Opção inválida, tente novamente')
            continue
        else:
            return n
        

def faixa_menu_candidatos(instrucoes="Digite um número numa faixa: "):
    while True:
        n = int(input(instrucoes))
        if n != 1 and n != 2 and n != 3 and n != 4:
            print('Opção inválida, tente novamente! ')
            continue
        else:
            return n
        

def obter_int(instrucoes="Digite um número inteiro: "):
    while True:
        try:
            n = int(input(instrucoes))
            return n
        except ValueError:
            print('Valor inválido, tente novamente! ')
            continue

def obter_real(instrucoes="Digite um número real: "):
    while True:
        try:
            n = float(input(instrucoes))
            return n
        except ValueError:
            print('Valor inválido, digite novamente ')
            continue


def validar_escala(instrucoes='Insira sua resposta: '):
    while True:
        escala = obter_int(instrucoes)
        if escala < 0 or escala > 6:
            print('Entrada inválida, tente novamente...')
            continue
        else:
            return escala
        


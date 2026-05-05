from utils import faixa_menu_inicial, faixa_menu_candidatos

def main():
    contador_validos = 0
    votos_candidato1 = 0
    votos_candidato2 = 0
    votos_candidato3 = 0
    votos_candidato4 = 0
    votos_brancos = 0
    votos_nulos = 0

    while True:
        menu_inicial()
        opcao = faixa_menu_inicial('>> ')

        if opcao == 7: #pra votar
            menu_candidatos()
            voto = faixa_menu_candidatos('Insira seu voto: ')
            contador_validos += 1

            if voto == 1:
                votos_candidato1 += 1
            elif voto == 2:
                votos_candidato2 += 1
            elif voto == 3:
                votos_candidato3 += 1
            elif voto == 4:
                votos_candidato4 += 1
            elif voto == 5:
                votos_nulos += 1
                contador_validos -= 1
            elif voto == 0:
                votos_brancos += 1
                contador_validos -= 1

        if opcao == -1: #-1 pra encerrar
            break
        if opcao == 6: 
            maior = maior_voto(votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4)
            percent1, percent2, percent3, percent4 = percent(votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4, contador_validos)
            print(f'''=============== RESULTADO ===============
Total de Votos Válidos ----- {contador_validos}
Total de votos brancos ----- {votos_brancos}
Total de votos nulos ----- {votos_nulos}
Percentual do candidato 1 ----- {percent1:.1f}
Percentual do candidato 2 ----- {percent2:.1f}
Percentual do candidato 3 ----- {percent3:.1f}
Percentual do candidato 4 ----- {percent4:.1f}''')
            print('Vencedores: ')
            mostrar_vencedores(maior, votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4)
            percent_maior = (maior / contador_validos) * 100 
            if percent_maior <= 50:
                print('Haverá segundo turno!')



def maior_voto(votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4):
    maior = votos_candidato1

    if votos_candidato2 > maior:
        maior = votos_candidato2
    if votos_candidato3 > maior:
        maior = votos_candidato3
    if votos_candidato4 > maior:
        maior = votos_candidato4
    return maior

def percent(votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4, contador_validos):
    percent1 = (votos_candidato1 / contador_validos) * 100
    percent2 = (votos_candidato2 / contador_validos) * 100
    percent3 = (votos_candidato3 / contador_validos) * 100
    percent4 = (votos_candidato4 / contador_validos) * 100
    return percent1, percent2, percent3, percent4

def mostrar_vencedores(maior, votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4):
    qtd_vencedores = 0
    if votos_candidato1 == maior:
        print('> Candidato 1')
        qtd_vencedores += 1
    if votos_candidato2 == maior:
        print('> Candidato 2')
        qtd_vencedores += 1
    if votos_candidato3 == maior:
        print('> Candidato 3')
        qtd_vencedores += 1
    if votos_candidato4 == maior:
        print('> Candidato 4')
        qtd_vencedores += 1
    if qtd_vencedores > 1:
        print('> Empate')


def menu_inicial():
    item1 = '=' * 30
    item2 = '-' * 10

    print(f'''=============== MENU ===============
Digite a opção desejada:
Votar {item2} 7
Ver Resultado {item2} 6
Encerrar {item2} -1
''')  


def menu_candidatos():
    item1 = '=' * 30

    print(f'''=============== CANDIDATOS ===============     
1 - Inácio Lula da Silva
2 - Pablo Marçal
3 - Bolsonaro
4 - Tábata Amaral
{item1}''') 

     
main()
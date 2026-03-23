def main():
    n_eleitores = int(input('Quantos eleitores? '))

    votos_eleitores(n_eleitores)


def votos_eleitores(n_eleitores):
    voto_candidato = 0
    voto_nulo = 0
    voto_branco = 0

    qtd_candidato1 = 0
    qtd_candidato2 = 0
    qtd_candidato3 = 0
   
    maior = 0
    vencedor = 0

    for i in range(1, n_eleitores + 1):
        voto_atual = int(input('Qual o seu voto? (1, 2, 3, 9, 0): '))

        if voto_atual > 0 and voto_atual <= 3:
            voto_candidato += 1
            if voto_atual == 1:
               qtd_candidato1 += 1 
               if qtd_candidato1 > maior:
                maior = qtd_candidato1
                vencedor = 1
            else:
                if voto_atual == 2:
                    qtd_candidato2 += 1
                    if qtd_candidato2 > maior:
                        maior = qtd_candidato2
                        vencedor = voto_atual
                if voto_atual == 3:
                    qtd_candidato3 += 1
                    if qtd_candidato3 > maior:
                        maior = qtd_candidato3
                        vencedor = voto_atual
                if qtd_candidato1 == qtd_candidato2 == qtd_candidato3:
                    vencedor = 'Empate'
                        
        elif voto_atual == 9:
            voto_nulo += 1
        elif voto_atual == 0:
            voto_branco += 1
    
    print(f'Total de votos para candidato: {voto_candidato}')
    print(f'Total de votos nulos: {voto_nulo}')
    print(f'Total de votos em branco: {voto_branco}')
    print(f'Vencedor: {vencedor}, com {maior} votos')


main()

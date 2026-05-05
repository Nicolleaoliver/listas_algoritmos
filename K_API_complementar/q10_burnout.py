from utils import obter_int, validar_escala

def main():
    n = obter_int('Quantos respondentes? ')
    
    maior_exaustao, menor_realizacao, media_geral, nome_maior_exaustao, nome_menor_realizacao = obter_respostas(n)
    print(f'''========== RESUMO DO ESTUDO ==========
Respondentes:     {n}
Maior Exaustão:     {nome_maior_exaustao} ({maior_exaustao:.2f})
Menor Realização:     {nome_menor_realizacao} ({menor_realizacao:.2f})
Média Geral Burnout:     {media_geral:.2f}''')


def obter_respostas(n):
    contador = 0
    escore_d1 = 0
    escore_d2 = 0
    escore_d3 = 0
    maior_exaustao = 0
    menor_realizacao = 0
    nome_maior_exaustao = None
    nome_menor_realizacao = None
    soma_escores = 0 

    for i in range(1, n + 1):
        nome = input('Seu nome: ')
        print('----- Dimensão 1 - Exaustão -----')
        q1_d1 = validar_escala('1. Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho.\n>>')
        q2_d1 = validar_escala('2. Sinto-me esgotado(a) ao final de um dia de estudos/trabalho.\n>>')
        q3_d1 = validar_escala('3. Acordar de manhã e ter que enfrentar mais um dia me causa cansaço.\n>>')

        print('----- Dimensão 2 - Despersonalização -----')
        q1_d2 = validar_escala('4. Sinto que me tornei mais indiferente com as pessoas ao meu redor.\n>>')
        q2_d2 = validar_escala('5. Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas.\n>>')
        q3_d2 = validar_escala('6. Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas.\n>>')

        print('----- Dimensão 3 - Realização Pessoal -----')
        q1_d3 = validar_escala('7. Consigo lidar eficazmente com os problemas que surgem no meu dia a dia.\n>>')
        q2_d3 = validar_escala('8. Sinto que estou tendo uma influência positiva na vida das pessoas.\n>>')
        q3_d3 = validar_escala('9. Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas.\n>>')
    
        escore_d1 = calcular_escores(q1_d1, q2_d1, q3_d1)
        escore_d2 = calcular_escores(q1_d2, q2_d2, q3_d2)
        escore_d3 = calcular_escores(q1_d3, q2_d3, q3_d3)

        exaustao, despersonalizacao, realizacao_pessoal = classificar_dimensao(escore_d1, escore_d2)
        exibir_laudo(nome, escore_d1, escore_d2, escore_d3, exaustao, despersonalizacao, realizacao_pessoal)

        if contador == 0:
            maior_exaustao = escore_d1
            nome_maior_exaustao = nome
            menor_realizacao = escore_d3
            nome_menor_realizacao = nome
        else:
            if escore_d1 > maior_exaustao:
                maior_exaustao = escore_d1
                nome_maior_exaustao = nome
            if escore_d3 < menor_realizacao:
                menor_realizacao = escore_d3
                nome_menor_realizacao = nome
        contador += 1
        soma_escores += (q1_d1 + q2_d1 + q3_d1) + (q1_d2 + q2_d2 + q3_d2)

    media_geral = soma_escores / (6 * n)
    return maior_exaustao, menor_realizacao, media_geral, nome_maior_exaustao, nome_menor_realizacao
            


def calcular_escores(q1, q2, q3):
    soma_escore = q1 +  q2 + q3
    escore = soma_escore / 3
    return escore
    

def classificar_dimensao(escore_d1, escore_d2):
    exaustao = None
    despersonalizacao = None
    realizacao_pessoal = None

    if escore_d1 <= 2:
        exaustao = 'Baixa'
        realizacao_pessoal = 'Alta'
    elif escore_d1 <= 3.9:
        exaustao = 'Moderada'
        realizacao_pessoal = 'Moderada'
    else:
        exaustao = 'Alta'
        realizacao_pessoal = 'Baixa'
    
    if escore_d2 <= 2:
        despersonalizacao = 'Baixa'
    elif escore_d2 <= 3.9:
        despersonalizacao = 'Moderada'
    else:
        despersonalizacao = 'Alta'
    
    return exaustao, despersonalizacao, realizacao_pessoal


def exibir_laudo(nome, escore_d1, escore_d2, escore_d3, exaustao, despersonalizacao, realizacao_pessoal):
    print(f'''========== LAUDO: {nome} ==========
Exaustão Emocional:     {escore_d1:.2f} - {exaustao}
Despersonalização:     {escore_d2:.2f} - {despersonalizacao}
Realização Pessoal:     {escore_d3:.2f} - {realizacao_pessoal}''')
    
    if (exaustao == 'Baixa' and despersonalizacao == 'Baixa') or (exaustao == 'Baixa' and realizacao_pessoal == 'Baixa') or (despersonalizacao == 'Baixa' and realizacao_pessoal == 'Baixa'):
        print('''Atenção: 2 dimensões em nível crítico.
Recomenda-se acompanhamento profissional.''')



if __name__ == '__main__':
    main()
def idade2(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    quant_anos1 = ano_atual * 365
    quant_meses1 = mes_atual * 30
    total_dias1 = quant_anos1 + quant_meses1 + dia_atual
    
    quant_anos2 = ano_nasc * 365
    quant_meses2 = mes_nasc * 30
    total_dias2 = quant_anos2 + quant_meses2 + dia_nasc

    subtracao = total_dias1 - total_dias2

    idade_anos = subtracao // 365
    resto = subtracao % 365
    idade_meses = resto // 30
    idade_dias = resto % 30

    return idade_anos, idade_meses, idade_dias


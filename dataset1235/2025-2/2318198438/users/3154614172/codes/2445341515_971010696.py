peso = float(input())
quantidade_diaria_em_gramas = float(input())

quantidade_usada_em_cinco_dias = quantidade_diaria_em_gramas * 5
quantidade_restante_apos_cinco_dias = peso - quantidade_usada_em_cinco_dias

print(round(quantidade_restante_apos_cinco_dias,3))
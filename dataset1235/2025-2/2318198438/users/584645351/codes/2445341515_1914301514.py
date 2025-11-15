valor_por_minuto = 0.28
consumo_de_chamadas = float(input())
assinatura = 23
total = consumo_de_chamadas*valor_por_minuto+assinatura
total_31 = total*0.31+total

print (round(total_31,2))
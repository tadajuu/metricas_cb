litros = float(input())

preco_litro = 2.86
troca_oleo = 50.00
icms_porcentagem = 34/100
total_bruto = (litros * preco_litro) + troca_oleo
icms = total_bruto * icms_porcentagem
total_final = total_bruto + icms
print(round(total_final,2))
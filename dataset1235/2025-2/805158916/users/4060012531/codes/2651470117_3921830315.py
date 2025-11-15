preco_gas=2.86
troca_oleo=50.0
icms=1.34

qtd_gas=float(input())

total=(qtd_gas*preco_gas+troca_oleo)*icms
print(round(total,2))


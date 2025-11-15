qty_abast=float(input("Digite a quantidade de litros abastecida: "))

preço_gas=qty_abast*2.86
troca_oleo=50.00
icms=(preço_gas+troca_oleo)*0.34

total=preço_gas+troca_oleo+icms

print(round(total,2))

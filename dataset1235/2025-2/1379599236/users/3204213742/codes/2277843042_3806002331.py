valor_gasolina = 2.86
troca_oleo = 50.00

l = float(input("quantidade:"))

valor_combutivel = valor_gasolina * l

total = (valor_combutivel + troca_oleo) * 1.34

print(round(total, 2))

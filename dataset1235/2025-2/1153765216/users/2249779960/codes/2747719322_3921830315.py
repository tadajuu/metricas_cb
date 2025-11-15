litros = float(input())
preco_gasolina = 2.86
troca_oleo = 50.00

subtotal = litros * preco_gasolina + troca_oleo
total = subtotal * 1.34

print(round(total, 2))
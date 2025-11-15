litros = float(input("Insira a quantidade de litros abastecidos: "))

preco_gasolina = 2.86
preco_litros = litros*preco_gasolina
preco_troca_de_oleo = 50.00
preco_total = (preco_litros+preco_troca_de_oleo)
preco_icms = (preco_total+(preco_total*(34/100)))

print(round(preco_icms,2))
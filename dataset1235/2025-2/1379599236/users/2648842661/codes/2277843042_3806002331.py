quantidade_de_litros = float(input("informe quantos litros de gasolina:"))

gasolina = ((quantidade_de_litros*2.86)+50)

valor_total = round(gasolina + gasolina*(34/100),2)

print(valor_total)
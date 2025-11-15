kWh = float(input("digite a quantidade de kWh consumida no mes:"))
ValorEnergia = 10 + 0.43*kWh
total = ValorEnergia + ValorEnergia*(25/100)
print(round(total,2))
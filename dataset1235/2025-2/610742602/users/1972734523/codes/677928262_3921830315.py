valor=float(input("Quantidade de litros de gasolina abastecido:"))

litro=2.86
oleo=50.00
icms=34/100

gasolina=valor*litro
servico=gasolina+oleo
total=servico*(1+icms)

print(round(total,2))
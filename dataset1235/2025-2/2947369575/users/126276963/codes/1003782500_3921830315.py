litros=float(input("Digite a quantidade de litros abastecidos:"))
preco_gasolina=2.86
valor_oleo=50.00
subtotal=(litros*preco_gasolina)+valor_oleo
icms=subtotal*(34/100)
total=subtotal+icms
print("O valor total a ser pago é:", round(total,2))
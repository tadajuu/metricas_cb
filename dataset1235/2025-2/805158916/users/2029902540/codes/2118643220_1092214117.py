QuantidadeDePedagios = float(input("Quantos pedagios tem?: "))
valorDoPedagio = 9.80
taxaFixa = 20.00
aumento = (15/100)
gastoA = valorDoPedagio + taxaFixa
#gasto1 =  valorDoPedagio + taxaFixa
#gasto2 = gasto1 * aumento
#final1 = gasto1 - gasto2
#gasto4 = final1 * QuantidadeDePedagios
#print(round(gasto4, 2))
gastoInicial = gastoA * aumento
gastofinal1 = gastoA  - gastoInicial
valorGasto = gastofinal1 * QuantidadeDePedagios
print(round(valorGasto , 2))
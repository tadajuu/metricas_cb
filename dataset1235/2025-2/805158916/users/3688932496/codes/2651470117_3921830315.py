#entrada : litros abastecidos.
litros = float(input("Informe a quantidade de litros anastecidos, e logo em seguinda iremos fornece o total a ser pago: "))
#valores fixos
gasolina = 2.86
troca_oleo = 50.0
icms_percentual = 34/100 #34%
#calculo do valor abastecido
valor_combustivel = litros * gasolina
#subtotal sem icms
subtotal = valor_combustivel + troca_oleo
#calculo do ICMS
icms = subtotal * icms_percentual
#total com icms
total_icms = subtotal + icms
#saida
print(round(total_icms,2))

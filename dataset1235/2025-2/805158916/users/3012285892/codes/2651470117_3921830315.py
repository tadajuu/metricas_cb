litro = float(input("Quantos litros"))

valor = litro*2.86 +50
imposto = valor*(34/100)
total = valor + imposto 

print(round(total,2))
peso = float(input("Digite o peso"))
frete = peso*43.21 
total = frete + 25 
icms = total * (62/100)
totalf = total + icms
print(round(totalf,2))
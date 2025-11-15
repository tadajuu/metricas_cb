peso = float(input())
frete = peso*43.21+25.00
icms= round(frete+ frete*(62/100), 2)
print(icms)
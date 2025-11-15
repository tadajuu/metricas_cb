NP = int(input("número de pedagios: "))
taxa = NP * 9.80
tf = 20.00
ICMS = (taxa + tf) * 15/100
vt = taxa + tf + ICMS

print(round(vt,2))
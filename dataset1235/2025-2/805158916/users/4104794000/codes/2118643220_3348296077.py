TE = int( input("Tempo no estacionamento"))
taxa = (TE* 15)
TF = 5.00
ICHS = ( taxa + TF)*(20/100)
V = (taxa + TF + ICHS)
print(round(V,2))
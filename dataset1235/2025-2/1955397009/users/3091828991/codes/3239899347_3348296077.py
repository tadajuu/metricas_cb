TE = int(input("Tempo no estacionamento em horas: "))
Taxa = (TE * 15)
TF = 5.00
ICMS = (Taxa + TF)*(20/100)
V = (Taxa + TF + ICMS)

print(round(V, 2))
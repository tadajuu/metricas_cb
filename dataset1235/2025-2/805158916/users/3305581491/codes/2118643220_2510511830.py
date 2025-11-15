minutos = float(input("Digite os minutos excedentes: "))
fixo = 45
excedente = minutos * 0.97
total = fixo + excedente
total_com_icms = total * 1.42
print(round(total_com_icms, 2))
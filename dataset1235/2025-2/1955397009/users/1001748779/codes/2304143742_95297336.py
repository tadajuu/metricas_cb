escala = input("Escala:").upper()
temp = float(input("Valor da temperatura:"))

if escala == "C":
  temp_saida = (9/5) * temp + 32
else:
  temp_saida = (5/9) * (temp - 32)

print(round(temp_saida, 2))
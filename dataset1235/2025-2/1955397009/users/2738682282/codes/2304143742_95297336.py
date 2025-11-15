escala = input("Qual escala está a temperatura: ").upper()
temp = float(input("Digite o valor da temperatura: "))

if escala == "F":
  temp_c = (5 / 9) * (temp - 32)
  print(round(temp_c, 2))
else: 
  temp_f = (temp * 9 / 5) + 32
  print(round(temp_f, 2))
  
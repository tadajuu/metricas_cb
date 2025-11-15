qj = int(input("Quantidade de sucos: "))
qs = int(input("Quantidade de salagados: "))
vd = float(input("Valor disponível: "))
if (qj * 3 + qs * 3.5 >= vd):
  print(round(qj * 3 + qs * 3.5,2))
  print("Nao")
else:
  print(round(qj * 3 + qs * 3.5,2))
  print("Sim")
num = int(input(print("Insira o numero de morangos: ")))
if num >= 12:
  total = num * 1.35
  print(round(total, 2))
else:
  total = num * 1.5
  print(round(total, 2))
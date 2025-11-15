consumo=float(input("consumo: "))

if (consumo<=150):
  total=consumo * 0.6 + 0.5
else:
  total= consumo * 0.75 + 16
  print(round(total,2))
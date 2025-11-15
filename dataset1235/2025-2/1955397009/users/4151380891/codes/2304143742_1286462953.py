consumo = float(input("consumo: "))

if (consumo <= 150):
  total = consumo * 0.6 + 5.0
else:
  total = consumo * 0.75 + 16.0

print(round(total,2 ))
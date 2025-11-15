c = float(input("Qual foi o consumo? "))
if c > 150:
  print(round(16.00 + 0.75 * c, 2))
else: 
  print(round(5 + 0.6 * c, 2))
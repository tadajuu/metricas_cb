a = float(input("Qual a area a ser plantada? "))
if a > 10000:
  print(round(5.00 * 10000 + 4.00 * (a - 10000), 2))
else: 
  print(round(5 * a, 2))
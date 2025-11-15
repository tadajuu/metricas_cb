m = int(input("Quantos morangos foram comprados? "))
if m < 12:
  print(round(m * 1.50, 2))
else:
  print(round(m * 1.35, 2))
morangos = int(input("Digite quantos morangos vc comprou: "))

if morangos < 12: 
  total = morangos * 1.50
  print(round(total, 2))
else: 
  total = morangos * 1.35
  print(round(total, 2))
x = int(input("Insira um numero de saida"))
y = int(input("divisor"))
if x%y == 0:
  print(x//y)
  print("sim")
else:
  print(x%y)
  print("nao")
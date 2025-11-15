x = int(input("Valor inteiro: "))
y = int(input("Divisor: "))
if (x % y == 0):
  print(x // y)
  print("sim")
else:
  print(x % y)
  print("nao")
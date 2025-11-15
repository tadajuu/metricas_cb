x = int(input("Insira um valor para x: "))
y = int(input("Insira um valor para y: "))

if x % y == 0:
  print(x // y)
  print("sim")
else:
  print(x % y)
  print("nao")
x = int(input("numero para X: "))
y = int(input("numero para Y: "))

if x%y == 0:
  print(x//y)
  print("sim")
else:
  print(x%y)
  print("nao")
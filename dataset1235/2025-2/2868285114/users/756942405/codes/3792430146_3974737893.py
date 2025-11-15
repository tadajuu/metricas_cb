x = int(input("x: "))
y = int(input("y: "))
if x%y == 0:
  print(x//y)
  print("sim")
else:
  print(x%y)
  print("nao")
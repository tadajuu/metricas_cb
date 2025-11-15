X = int(input("X: "))
Y = int(input("Y: "))

if X % Y == 0:
  print(X//Y)
  print("sim")
else:
  print(X%Y)
  print("nao")
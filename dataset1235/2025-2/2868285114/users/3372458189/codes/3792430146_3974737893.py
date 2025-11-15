X = int(input("Digite o numero X: "))
Y = int(input("Digite o divisor Y: "))
if X%Y == 0:
  print(X//Y)
  print("sim")
else: 
  print(X%Y)
  print("nao")
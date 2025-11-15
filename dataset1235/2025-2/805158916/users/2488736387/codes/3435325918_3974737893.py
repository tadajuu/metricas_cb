X = int(input("Insira um numero inteiro: "))
Y = int(input("divisor "))

if X % Y==0:
  print(X//Y)
  print("sim")
else:
  print(X%Y)
  print("nao")
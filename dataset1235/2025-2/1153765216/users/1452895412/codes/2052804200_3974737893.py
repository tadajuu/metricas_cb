X = int(input(print("Insira o numero inteiro: ")))
Y = int(input(print("Insira o divisor: ")))
if X % Y == 0:
  print(X // Y)
  print("sim")
else:
  print(X % Y)
  print("nao")
n_X = int(input("Qual o numero?: "))
n_Y = int(input("Qual o outro numero?: "))

if n_X % n_Y == 0:
  divisao = n_X // n_Y
  print(divisao)
  print("sim")

else:
  print(n_X % n_Y)
  print("nao")
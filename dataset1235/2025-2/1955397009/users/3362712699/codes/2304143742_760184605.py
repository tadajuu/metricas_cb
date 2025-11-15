s0 = int(input("Qual a posição inicial do objeto? "))
v = int(input("Qual a velocidade do objeto? "))
t = int(input("Qual o tempo de deslocamento? "))
S = s0 + v * t

if S < 1000:
  print(S)
  print("Nao")
else: 
  print(S)
  print("Sim")
  
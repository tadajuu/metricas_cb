x = int(input())
y = int(input())

quociente_da_divisao_inteira = (x // y)
resto_da_divisao = (x % y)


if(resto_da_divisao == 0):
  print(quociente_da_divisao_inteira)
  print("sim")
else:
  print(resto_da_divisao )
  print("nao")
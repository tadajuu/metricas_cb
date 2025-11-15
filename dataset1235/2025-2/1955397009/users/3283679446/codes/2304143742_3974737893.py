x = int(input("Insira um número inteiro: "))
y = int(input("Insira um número inteiro: "))

resto = x % y
quociente = x // y

if resto == 0:
  print(quociente)
  print("sim")
else:
  print(resto)
  print("nao")
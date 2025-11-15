x = int(input("digite um número: "))
y = int(input("digite um número: "))
quonci = x // y
resto = x % y
if x % y == 0:
  print(f"{quonci}")
  print("sim")
else:
  print(f"{resto}")
  print("nao")
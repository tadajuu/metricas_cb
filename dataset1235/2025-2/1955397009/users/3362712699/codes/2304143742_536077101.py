lanche = input("Vocês pedirão bolo(digite B) ou salgado(digite S)? ")
q = int(input("Qual a quantidade? "))
r = int(input("Qual a quantidade de refrigerantes? "))
v = float(input("Qual o valor que vocês têm? "))

if lanche == "B":
  print(round(2.5 * q + 3.00 * r, 2))
  if (2.5 * q + 3.00 * r) < v:
    print("Sim")
  else:
    print("Nao")
else:
  print(round(3.5 * q + 3.00 * r, 2))
  if (3.5 * q + 3.00 * r) < v:
    print("Sim")
  else:
    print("Nao")
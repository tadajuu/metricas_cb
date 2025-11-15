s = int(input("Digite a quantidade de sucos comprados: "))
r = int(input("Digite a quantidade de salgados comprados: "))
v = float(input("Quanto vocês tem? "))

print(3.00 * s + 3.50 *  r)

if (3.00 * s + 3.50 *  r) < v:
  print("Sim")
else:
  print("Nao")

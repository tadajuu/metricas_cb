suco = int(input("suco: "))
salgado = int(input("salgado: "))
valor = float(input("valor: "))
total = suco * 3.00 + salgado * 3.50
print(round(total, 2))
if total > valor:
  print("Nao")
else:
  print("Sim")
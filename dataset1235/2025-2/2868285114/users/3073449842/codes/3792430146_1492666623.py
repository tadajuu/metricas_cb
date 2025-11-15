suco = int(input(""))
salgado = int(input(""))
disponivel = float(input(""))
total = suco*3+salgado*3.5
print(round(total, 2))
if disponivel-total>=0:
  print("Sim")
else:
  print("Nao")
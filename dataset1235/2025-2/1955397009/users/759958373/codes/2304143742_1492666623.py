suco = int(input())
saguado = int(input())
denhero = float(input())
total = suco*3 + saguado*3.5
if(denhero <= total):
  print(round(total, 2))
  print("Nao")
else:
  print(round(total, 2))
  print("Sim")
Qsuco = int(input())
Qsalgado = int(input())
dinheiros = float(input())

Tsuco = Qsuco * 3.00
Tsalgado = Qsalgado *3.50
total = Tsuco + Tsalgado

print (total)
if (dinheiros > total):
  print("Sim")

else: 
  print("Nao")
  

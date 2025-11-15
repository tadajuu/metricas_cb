su = int(input())
sa = int(input())
vd = float(input())

vt = su*3+sa*3.50
print(round(vt,2))
if vd-vt>=0:
  print("Sim")
else:
  print("Nao")
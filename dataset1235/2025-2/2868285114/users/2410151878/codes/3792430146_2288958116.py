q=int(input("digite a quantidade de jogos: "))
p1=float(input("digite valor: "))

if q==1:
  total=p1
else:
  p2=float(input("digite o valor: "))
  total= p1 + p2 * 0.75

print(round(total,2))
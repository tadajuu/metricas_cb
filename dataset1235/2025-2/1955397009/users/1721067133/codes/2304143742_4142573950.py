n = int(input())

if n >= 12:
  vcompra = 1.35 * n
  print(round(vcompra,2))
else:
  vcompra = 1.50 * n
  print(round(vcompra,2))
tipo = input()
tipo.upper()

valor = float(input())

if tipo == "F":
  temperatura = (valor - 32) * 5 / 9

elif tipo == "C":
  temperatura = valor * (9/5) + 32

print(round(temperatura, 2))
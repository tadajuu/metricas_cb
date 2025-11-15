escala = input()
temp = float(input())

if escala == 'C':
  saida = (temp * 9/5) + 32
  print(round(saida,2))
else:
  saida1 = (temp - 32) * 5/9
  print(round(saida1,2))
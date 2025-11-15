Temp = input()
valor = float(input())

if(Temp == "C"):
  print(round((valor*(9/5))+32, 2))
if(Temp == "F"):
  print(round(5/9*(valor-32), 2))
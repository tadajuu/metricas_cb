x = int(input("insira o numero: "))
y = int(input("numero: "))
r = x%y 
s = x//y
if r == 0 : 
  print(s)
  print("sim")
else : 
  print(r)
  print("nao")
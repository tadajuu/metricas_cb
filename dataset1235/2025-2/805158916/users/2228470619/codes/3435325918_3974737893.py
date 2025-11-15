x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))

if(x%y==0):
  print(x//y)
  print("sim")

else:
  print(x%y)
  print("nao")
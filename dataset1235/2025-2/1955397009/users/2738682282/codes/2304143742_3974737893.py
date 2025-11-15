x = int(input("Qual o número x: "))
y = int(input("Qual o número y: "))

if (x % y == 0): 
  quociente = x // y
  print(quociente)
  print("sim")
else: 
  resto = x % y
  print(resto)
  print("nao")
  
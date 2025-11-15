escala = input().upper()
temp = float(input())

if (escala == "C"):
  conversao = (9/5)*temp +32
  print(round(conversao,2))
  
elif (escala == "F"):
  conversao = (5/9)*(temp - 32)
  print(round(conversao,2))

else:
 print("escala errada")
x=int(input())
y=int(input())
z=x%y
if (z == 0):
  print(round(x//y))
  print("sim")
else:
  print(round(x%y,0))
  print("nao")
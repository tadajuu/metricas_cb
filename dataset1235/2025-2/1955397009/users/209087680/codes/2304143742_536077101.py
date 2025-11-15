x=input()
y=int(input())
z=float(input())
a=float(input())
c=(z*3)
if (x=='S'):
  b=(y*3.50)
else:
  b=(y*2.50)

  
if (b+c<a):
  print(b+c)
  print("Sim")
else:
  print(b+c)
  print('Nao')
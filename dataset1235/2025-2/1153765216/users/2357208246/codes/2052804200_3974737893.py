x = int(input())
y = int(input())
resto = x%y
if(resto == 0):
  print(x//y)
  print('sim')
else:
  print(resto,'nao')
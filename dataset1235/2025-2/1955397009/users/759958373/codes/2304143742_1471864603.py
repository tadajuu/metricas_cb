area = float(input())

if(area <= 10000):
  total = area*5
else:
  total = (area-10000)*4 + 10000*5

print(round(total, 2))
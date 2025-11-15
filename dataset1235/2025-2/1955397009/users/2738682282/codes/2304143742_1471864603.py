area = float(input())

if area <= 10000: 
  total = area * 5
  print(round(total, 2))
else: 
  exc = area - 10000
  total = 10000 * 5 + exc * 4
  print(round(total, 2))
  
  
  
cons = float(input())

if cons <= 150:
  total = cons * 0.60 + 5.00
else:
  total = cons * 0.75 + 16.0

print(round(total,2))
con=float(input("digte seu consumo: "))

if con <= 150:
  total=con*0.60+5.0
else:
  total=con*0.75+16

print(round(total,2))
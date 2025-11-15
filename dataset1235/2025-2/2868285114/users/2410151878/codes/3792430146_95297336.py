es=input("C ou F:")
tp=float(input("digite a temperatura: "))

if es == "C":
  cel = (tp * 9.0/5.0)+ 32.0
  print(round(cel,2))
else:
  feh = (tp - 32)* 5/9
  print(round(feh,2))
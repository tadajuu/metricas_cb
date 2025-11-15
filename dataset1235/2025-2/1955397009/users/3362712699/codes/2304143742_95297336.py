escala = input("Qual a escala da temperatura? ").upper()
ti = float(input("Qual a temperatura? "))

if escala == "C":
  tf = (9/5) * ti +32
else:
  tf = (5/9) * (ti - 32)

print(round(tf, 2))
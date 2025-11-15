Escala = input("Qual a escala? (F) ou (C)?: ").upper()
valor = float(input("Qual o valor da temperatura?: "))

if Escala == "C":
  Farenheit = (valor * 9/5) + 32
  print(round(Farenheit, 2))

else:
  Celsius = (valor - 32) * 5/9
  print(round(Celsius, 2))
  
escala = input("Escala(Se for Celsius 'C', se for Fahrenheit 'F': ").upper()
te = float(input("Valor da temperatura: "))
if (escala == "C"):
  ts = (9 / 5) * te + 32
  
else:
  ts = (5 / 9) * (te - 32)
print(round(ts,2))
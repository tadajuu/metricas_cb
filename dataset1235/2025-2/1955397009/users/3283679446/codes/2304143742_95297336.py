escala = input("Informe a escala Celsius ou Fahrenheit - digite C/F: ")
temperatura = float(input("Informe a temperatura: "))

fah_cel = 5/9 * (temperatura - 32)
cel_fah = (temperatura * (9/5)) + 32

if escala.upper() == "C":
  print(round(cel_fah, 2))
  
elif escala.upper() == "F":
  print(round(fah_cel, 2))
  
else:
  print("Reinicie o programa e insira as informações corretamente.")





def conversor(celsius):
  kelvin = celsius + 273.15
  return round(kelvin, 2)

temp = float(input("Digie a temperatura em C: "))

res = conversor(temp)
print(res)
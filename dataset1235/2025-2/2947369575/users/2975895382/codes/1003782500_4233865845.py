
def converteCtoF(temp):
  fahr = (temp * 9/5) + 32
  return round(fahr, 2)

celsius = float(input("Digite a temperatura a ser convertida: "))

res = converteCtoF(celsius)
print(res)
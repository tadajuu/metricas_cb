escala = input("Informe a escala da temperatura: ").upper()
valor = float(input("Informe o valor da temperatura: "))

if(escala=="C"):
  print("Temperatura em Farenheit: ",round(32+(1.8*valor),2))

else:
  print("Temperatura em Celsius: ",round((5/9)*(valor-32),2))
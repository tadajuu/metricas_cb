#Entrada de dados
celsius = float(input("Digite a temperatura em celsius: "))

#Conversão para Kelvin
kelvin = celsius + 273.15

#Saída com 2 casas decimais
print("Temperatura em kelvin: {:.2f}".format(kelvin))
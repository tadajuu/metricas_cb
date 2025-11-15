# Programa que converte Celsius em Fahrenheit

# Lendo a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

#Convertendo para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Imprimindo o resultado arredondado para duas casas decimais
print("Temperatura em Fahrenheit:", round(fahrenheit, 2))
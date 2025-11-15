# Programa que converte Celsius em Fahrenheit
#Lendo a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))
#Convertendo para fahrenheit 
fahrenheit = (celsius * 9/5) + 32
#Imprimindo o resuktadi arredondado para 2 casas decimais 
print("Temperatura em Fahrenheit:", round(fahrenheit, 2))
# Programa que converte celsius em fahrenheit
# Lendo a temperatura em celsius
celsius = float(input("Digite a temperatura em celsius: "))
# COnvertendo para fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
# Imprimindo o resultado arredondado para 2 casas decimais
print("Temperatura em fahrenheit:", round(fahrenheit, 2))
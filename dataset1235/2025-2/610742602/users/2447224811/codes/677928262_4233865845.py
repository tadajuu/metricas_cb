#Leitura da temperatura em celsius 
celsius = float(input("digite a temperatura em celsius: "))
#Conversão para fahrnheit
fahrenheit = (celsius * 9/5 )+ 32 
# Exibir resultado arredondado para duas casas decimais
print(round(fahrenheit, 2 ))
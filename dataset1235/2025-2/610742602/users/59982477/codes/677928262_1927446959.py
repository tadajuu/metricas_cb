#Leitura da entrada
n = float(input())
#1. Calcular 27% de n 
valor1 = n * (27/100)
#2. Calcular n acrescido de 42%
valor2 = n + n * (42/100)
#3. Calcular n com desconto de 63%
valor3 = n - n * (63/100)
#Imprimir resultados arredondados com 2 casas decimais 
print(round(valor1, 2))
print(round(valor2, 2))
print(round(valor3, 2))

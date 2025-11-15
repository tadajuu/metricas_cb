#Início
numero = float(input("Insira o número: "))
#27% do valor
EQ = numero * (27/100)
#Valor acrescido de 42%
VQ = numero + (numero * (42/100))
#Valor com desconto de 63%
DQ = numero - (numero * 63/100)
#Impressão dos valores
print(round(EQ,2))
print(round(VQ,2))
print(round(DQ,2))
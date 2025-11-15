n = float(input("digite o litro: "))
#preço do litro
L = 2.86
#Custo do litro
c = n * L
#Preço da troca de oléo
o = 50.00
x = c + o
ICMS = x*(34/100)
print (round(x + ICMS, 2))
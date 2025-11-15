#quantidade de litros de gasolina comprados
x = float(input("litros: "))
#preco por litro
w = x*2.86
#valor da troca de óleo 
y = 50.0
#preco sem o ICMS
p = w+y
#ICMS
ICMS = p*0.34

print(round(p+ICMS, 2))

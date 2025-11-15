
#Objetivo: 
#1. Calcular 27% do valor de entrada
#2. total + 42% de n
#3. total - 63% de n
def promocao1(valor):
  parcial = 0.27*valor
  return round(parcial, 2)

def promocao2(valor):
  juros = 0.42 * valor
  total = valor + juros
  return round(total,2)

def promocao3(valor):
  desconto = 0.63 * valor
  total = valor - desconto
  return round(total, 2)

n = float(input("Digite um valor para comecar o programa: "))

res1 = promocao1(n)
res2 = promocao2(n)
res3 = promocao3(n)

print(res1)
print(res2)
print(res3)


  
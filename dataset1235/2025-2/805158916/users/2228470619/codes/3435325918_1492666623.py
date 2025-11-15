suco = int(input("Informe a quantidade de suco: "))
salga = int(input("Informe a quantidade de salgados: "))
valor = float(input("Informe o valor disponível: "))
valsuco = suco*3
valsal = salga*3.50

if(valor>=valsuco+valsal):
  print("Valor total: ",round(valsuco+valsal,2))
  print("Sim")

else:
  print("Valor total: ",round(valsuco+valsal,2))
  print("Nao")
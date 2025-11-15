quantidade_combustivel = float(input("digite o  litro: "))
#preço do litro
preco_litro= 2.86 
#custo do litro
custo_combustivel = quantidade_combustivel * preco_litro
#preço da troca de oleo
custo_troca_oleo = 50.00
custo_combustivel_e_oleo = custo_troca_oleo + custo_combustivel
icms = custo_combustivel_e_oleo*(34/100)
total= custo_combustivel_e_oleo + icms
print (round(total,2))
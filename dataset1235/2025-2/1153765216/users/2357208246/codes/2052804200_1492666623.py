qtd_sucos = int(input())
qtd_salgados = int(input())
valor_disponivel = float(input())

preco_suco = qtd_sucos * 3
preco_salgado = qtd_salgados * 3.5
preco_lanche = preco_salgado+preco_suco
print(round(preco_lanche, 2))
if preco_lanche >= valor_disponivel:
  print('Nao')
else: 
  print('Sim')
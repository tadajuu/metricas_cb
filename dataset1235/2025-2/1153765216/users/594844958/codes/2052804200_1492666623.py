qnt_sucos = int(input())
qnt_salgados = int(input())

valor_disponivel = float(input())

valor_total = (qnt_sucos * 3) + (qnt_salgados * 3.50)

print(round(valor_total, 2))

if valor_disponivel >= valor_total:
  print("Sim")

else: 
  print("Nao")
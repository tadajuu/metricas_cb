quant_sucos = int(input())
quant_salgados = int(input())
valor_disponivel = float(input())

total = quant_salgados * 3.50 + quant_sucos * 3
diferenca = valor_disponivel - total

print(round(total, 2))
if diferenca >= 0:
  print("Sim")
else:
  print("Nao")
  
quant_suco = int(input())
quant_salgados = int(input())
money = float(input())

valor_suco = quant_suco*3.00
valor_salgado = quant_salgados*3.50

valor_total = valor_suco + valor_salgado

print(valor_total)

if (money >= valor_total):
  print("Sim")
else:
  print("Nao")
mimida = input()
quant_mimida = int(input())
quant_refri = int(input())
valor = float(input())

if(mimida == "B"):
  valor_mimida = quant_mimida*2.5
if(mimida == "S"):
  valor_mimida = quant_mimida*3.5

total = valor_mimida + quant_refri*3

if(valor >= total):
  print(round(total, 2))
  print("Sim")
else:
  print(round(total, 2))
  print("Nao")
quant_suco = int(input("quant_suco: "))
quant_salgado = int(input("quant_salgado: "))
valor_disponivel = float(input("digite o valor disponivel: "))
valortotal=(3.50 * quant_salgado) + (3.00 * quant_suco)
valortotalarredondado = round(valortotal,2)
print(valortotalarredondado)
if valortotalarredondado > valor_disponivel:
  print("Nao")
else:
  print("Sim")
qtd_s = int(input("Quantidade de suco: "))
qtd_sa = int(input("Quantidade de salgado: "))
valor_disp = float(input("Digite o valor disponível: "))
valortotal = (3.00 * qtd_s) + (3.50 * qtd_sa)
valortotalarredondado = round(valortotal,2)
print(valortotalarredondado)
if valortotalarredondado > valor_disp:
  print("Nao")
else:
  print("Sim")
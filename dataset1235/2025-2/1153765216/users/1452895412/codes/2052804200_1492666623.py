suco = int(input(print("Insira a quantidade de sucos: ")))
salgado = int(input(print("Insira a quantidade de salgados: ")))
valor = float(input(print("Insira o valor disponivel: ")))
total = (suco * 3) + (salgado * 3.5)
print(round(total, 2))
if valor >= total:
  print("Sim")
else:
  print("Nao")
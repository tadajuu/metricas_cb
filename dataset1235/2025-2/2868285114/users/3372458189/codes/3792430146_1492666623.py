suco = int(input("Digite a quantidade de sucos: "))
salgado = int(input("Digite a quantidade de salgados: "))
disponivel = float(input("Digite o valor disponivel: "))
total = salgado*3.50+suco*3
print(round(suco*3+salgado*3.50, 2))
if disponivel-total >=0:
  print("Sim")
else:
  print("Nao")
# o programa vai fala sim ser de para paga . caso contrario "não"
suco = float(input("Informe a quanidade de sucos pedidos:"))
salg = float(input("Informe a quantidade de salgaos pedidos:"))
valor_disp = float(input("Informe o valor disponível para o pagamento:"))
 
valor_total = (suco * 3) + (salg * 3.5)

if (valor_total > valor_disp):
  print(round(valor_total,2))
  print("Nao")
else:
  print(round(valor_total,2))
  print("Sim")
  

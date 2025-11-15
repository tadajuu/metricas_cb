
var = input("Digite B se for um bolo ou S se for um salgado: ").upper()
quantidade = int(input("Digite a quantidade de bolos ou salgados: "))
refrigerante = int(input("Digite a quantidade de refrigerante: "))
valor = float(input("Digite o valor disponivel: "))

if var == "B": 
  total = quantidade * 2.50 + refrigerante * 3
  print(round(total, 2))
  
  if total > valor: 
    print("Nao")
  else:
    print("Sim")
else:
  total = quantidade * 3.50 + refrigerante * 3
  print(round(total, 2))

  if total > valor: 
    print("Nao")
  else:
    print("Sim")

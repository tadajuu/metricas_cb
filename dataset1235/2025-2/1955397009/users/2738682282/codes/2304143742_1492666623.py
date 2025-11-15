suco = int(input("Digite a quantidade de sucos: "))
salgado = int(input("Digite a quantidade de salgados: ")) 
valor = float(input("Digite o valor disponível: "))

valor_suco = suco * 3
valor_salgado = salgado * 3.50

total = valor_suco + valor_salgado

if total > valor:
  print(round(total, 2))
  print("Nao")
else: 
  print(round(total, 2))
  print("Sim")

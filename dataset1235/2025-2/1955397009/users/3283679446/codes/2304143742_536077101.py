bolo_salgado = input("Escreva S se quiser salgado e B se quiser bolo: ")

if bolo_salgado.upper() == "B":
  bolo = int(input("Quantos bolos:"))
  refri = int(input("Quantos refrigerantes:"))
  valor = float(input("Qual o valor disponível: "))
  total = 3 * refri + 2.50 * bolo
  print(round(total, 2))
  diferenca = valor - total
  if diferenca >= 0:
    print("Sim")
  else:
    print("Nao")
else:
  salgados = int(input("Quantos salgados:"))
  refri = int(input("Quantos refrigerantes:"))
  valor = float(input("Qual o valor disponível: "))
  total = 3 * refri + 3.50 * salgados
  print(round(total, 2))
  diferenca = valor - total
  if diferenca >= 0:
    print("Sim")
  else:
    print("Nao")
  
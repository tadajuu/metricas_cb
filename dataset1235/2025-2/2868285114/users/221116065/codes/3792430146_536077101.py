Refri = 3.00
Bolo = 2.50
Salgado = 3.50

comida = input("Qual o produto? (B ou S)?: ").upper()
quantidade = int(input("Qual a quantidade?: "))
quantidade_refri = int(input("Qual a quantidade de refrigerante?: "))
disponivel = float(input("Qual o valor disponivel?: "))

if comida == "B":
  calculo = (Bolo * quantidade) + (Refri * quantidade_refri)
  if disponivel >= calculo:
    print(calculo)
    print("Sim")
  else:
    print(calculo)
    print("Nao")

else:
  calculo = (Salgado * quantidade) + (Refri * quantidade_refri)
  if disponivel >= calculo:
    print(calculo)
    print("Sim")
  else:
    print(calculo)
    print("Nao")
  


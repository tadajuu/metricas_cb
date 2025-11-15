entradaSt = input().upper()
quantidadeX = int(input())
quantidadeRef = int(input())
dinheiro = float(input())

if (entradaSt=="B"): #pra entrada de B
  valorX = quantidadeX * 2.50 #calculo de bolo
elif (entradaSt=="S"): #segunda condição pra quando for salgado
  valorX = quantidadeX * 3.50  #calculo de salgado
else: #auto explicativo
  print("string nao encontrada")
  exit() #encerra o programa na hr e não vai fazer o restante do calculo
VT = valorX + (quantidadeRef * 3.00)
print(round(VT,2))


if (dinheiro > VT ): #condição pra se eles conseguem pagar o Zezinho
  print("Sim") 
else:
  print("Nao")
  





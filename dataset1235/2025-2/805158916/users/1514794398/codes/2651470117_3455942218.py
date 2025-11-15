valor1 = float(input("Qual o valor unitario do jogo?"))
valor0 = float(input("Qual o valor disponivel para a aquisicao do jogo?"))
total = valor1*8 + 45
saldo = valor0 - total

print(round(total,1))
print(round(saldo,1))

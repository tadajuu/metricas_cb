preço= float(input("Qual o valor unitario do jogo? "))
limite= float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = preço*8+45
saldo = limite-total

print(round(total,1))
print(round(saldo,1))
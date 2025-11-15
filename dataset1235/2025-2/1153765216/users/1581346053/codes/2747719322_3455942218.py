ValorUnit = float(input("Qual o valor unitario do jogo? "))
Valortotal = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = round((ValorUnit * 8 + 45), 1)
saldo = round((Valortotal - total), 1)

print(total)
print(saldo)
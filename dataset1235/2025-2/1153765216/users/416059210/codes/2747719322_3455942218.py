jogos = float(input("Qual o valor unitario do jogo? "))
disp = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

total = (jogos *8) + 45
saldo = disp - total
        
print(round(total,2))
print(round(saldo,2))
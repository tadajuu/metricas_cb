vu=float(input("Qual o valor unitario do jogo?:"))
vd=float(input("Qual o valor diposnivel para a aquisicao dos jogos?:"))
total=vu*8+45
saldo=vd-total
print(round(total,1))
print(round(saldo,1))
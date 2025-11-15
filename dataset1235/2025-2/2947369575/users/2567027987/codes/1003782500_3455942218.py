valoruni = float(input("Qual o valor unitario do jogo? "))
valordis = float(input("Qual o valor diposnivel para a aquisicao dos jogos? "))

tax = 45
total = 8*valoruni + tax
resto = valordis-total
print(round(total,1))
print(round(resto,1))
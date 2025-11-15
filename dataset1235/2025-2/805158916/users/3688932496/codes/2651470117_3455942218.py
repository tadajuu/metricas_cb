#valor unitario do jogo
valor_jogo = float(input("Digite o valor unitário do jogo:"))
#valor disponiivel para a compra
print("")
valor_disponivel = float(input("Digite o valor disponível para a compra:"))
#valor total das compras
frente = 45.0
quantidade_jogos = 8
total = (valor_jogo * quantidade_jogos) +frente
# valor restante
saldo = valor_disponivel - total
print("")
#saidas
print(round(total,1))
print(round(saldo,1))
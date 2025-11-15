
valor_unitario= float(input("Digite o valor unitario do jogo: R$ "))
dinheiro_disponivel=float(input("Digite o valor disponivel para a compra: R$ "))

quantidade_jogos=8
valor_frete=45.00

valor_total_jogos=valor_unitario*quantidade_jogos
valor_total_compra=valor_total_jogos+valor_frete
dinheiro_restante=dinheiro_disponivel-valor_total_compra

print(round(valor_total_compra,1))
print(round(dinheiro_restante,1))
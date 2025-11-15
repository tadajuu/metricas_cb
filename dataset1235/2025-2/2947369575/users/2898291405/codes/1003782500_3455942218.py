valor_jogo = float(input("Qual o valor initario do jogo? "))
valor_disponível = float(input("Qual o valor disponivel para aquisicao dos jogos? "))

total = (valor_jogo * 8) + 45
saldo = valor_disponível - total

print(f"{total:.1f}")
print(f"{saldo:.1f}")
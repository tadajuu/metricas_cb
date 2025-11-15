quantidade = int (input("Informe a quantidade de jogos:"))
print("")
#segundo
valor_unitario = float(input("Digite o valor unitário do jogo:"))
print("")
frente = float(input("informe o valor do frente: "))
print("")
total = (quantidade * valor_unitario) + frente
print(round(total,1))
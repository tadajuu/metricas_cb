quantidadeJogos = int(input())
valorUnitario = float(input())
valorFrete = float(input())

total = (quantidadeJogos * valorUnitario) + valorFrete
print(round(total, 2))
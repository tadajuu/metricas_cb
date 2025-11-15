pesoDoSaco = float(input("quantidade de peso: "))
quantidadeDiaria = float(input("Quantidade de gramas diarias: "))
QuantidadeApos5Dias = quantidadeDiaria * 5 
print(round(pesoDoSaco - QuantidadeApos5Dias, 2))
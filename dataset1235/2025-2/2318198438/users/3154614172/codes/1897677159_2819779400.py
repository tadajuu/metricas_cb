# Leitura das entradas e conversão para float.
quantidade = float(input('Quantas unidades você quer comprar?'))
valor = float(input('Qual o valor do jogo?'))
frete = float(input('Qual o valor do frete?'))

# Cálculo do toal a ser pago na compra.
total = quantidade*valor + frete

# Impressão do total a ser pago na compra.
print(total)
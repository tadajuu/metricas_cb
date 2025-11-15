
# Leitura das entradas e conversao para float:
num1 = float(input("Qual o valor unitario do jogo? "))
num2 = float(input("Qual o valor disponivel para a aquisicao dos jogos? "))

# Calculo do valor a ser pago, incluindo o frete:
frete = 45
jogos = 8

total_unitario = num1 * jogos
total_frete = total_unitario + frete

saldo =  num2 - total_frete

# Saída
print(round(total_frete, 1))
print(round(saldo, 1))
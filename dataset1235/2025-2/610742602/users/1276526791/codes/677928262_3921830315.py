# Preços fixos
preco_litro = 2.86
troca_oleo = 50.0
icms = 34 # em porcentagem
# Lendo a quantidade de litros abastecidos
litros = float(input())
# Calculando o total antes do imposto
total = (litros * preco_litro) + troca_oleo
# Aplicando o icms de 34%
total_com_imposto = total * (1 + icms / 100)
# Imprimindo o valor total arredondado para 2 casas decimais
print(round(total_com_imposto, 2))
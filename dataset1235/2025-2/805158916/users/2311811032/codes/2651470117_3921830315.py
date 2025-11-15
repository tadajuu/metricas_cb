# Pagando a gasolina

# 1 Entrada
litros = float(input('5'))

# 2 Valores fixos
preco_gasolina = 2.86
troca_oleo = 50.0

# 3 Total sem imposto
total = litros * preco_gasolina + troca_oleo

# 4 ICMS de 34%
total_com_icms = round(total * (1 + 34/100), 2)

# 5 Saida 
print(total_com_icms)
# Entrada da quantidade de litros abastecidos
litros = float(input())

# Calcular o valor do abastecimento
valor_gasolina = litros * 2.86

# Calcular o valor total dos serviços (gasolina + troca de óleo)
valor_servicos = valor_gasolina + 50.00

# Calcular o ICMS (34% sobre o valor dos serviços)
icms = valor_servicos * 0.34

# Calcular o valor total a ser pago
total_pagar = valor_servicos + icms

# Arredondar para duas casas decimais e imprimir
print(round(total_pagar, 2))
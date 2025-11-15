qtd_litros = float(input())
preco_litro = 2.86
troca_oleo = 50.00
icms = 0.34

valor_servicos = qtd_litros * preco_litro + troca_oleo
valor_total = valor_servicos + valor_servicos * icms

print(round(valor_total, 2))
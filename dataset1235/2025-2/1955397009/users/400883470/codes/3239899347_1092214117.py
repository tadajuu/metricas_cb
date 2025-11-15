qtd_pedagio = int(input())
valor_total = (9.80 * qtd_pedagio) + 20.00
total_imposto = valor_total + (valor_total*0.15)
print(round(total_imposto,2))
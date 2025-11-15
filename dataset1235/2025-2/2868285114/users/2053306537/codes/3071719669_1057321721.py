preco_por_m3 = 0.37
taxa_fixa = 15.00
aliquota_icms = 0.35
volume = float(input())
subtotal = volume * preco_por_m3 + taxa_fixa
total = subtotal * (1 + aliquota_icms)
total = round(total, 2)
print(f"{total:.2f}")
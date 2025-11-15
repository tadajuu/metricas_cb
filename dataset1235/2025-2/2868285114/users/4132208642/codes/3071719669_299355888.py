tempo = float (input())
total_gasto = tempo *50+30
icms = total_gasto * 0.18

total = icms + total_gasto
print(round(total,1))
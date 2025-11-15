bolas = int(input())
valor_sem_desconto = float(input())

if bolas >= 3:
  valor_total = float(valor_sem_desconto - 2)
else:
  valor_total = float(valor_sem_desconto)

print(f"{valor_total:.2f}")
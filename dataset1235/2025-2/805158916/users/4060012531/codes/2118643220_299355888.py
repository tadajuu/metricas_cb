dias=int(input())
alug_dias=50*dias
tax=30
icms=(alug_dias+tax)*.18
total_aluguel=alug_dias+tax+icms
print(total_aluguel)

def calcula_custo(valor_pizza: int, qtd_unitario: int) -> int:
  return valor_pizza * qtd_unitario

total_gasto = calcula_custo(35, 20)
print(total_gasto)
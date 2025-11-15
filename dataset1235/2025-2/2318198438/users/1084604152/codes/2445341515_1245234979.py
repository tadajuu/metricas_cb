peso_total = float(input())
qtd_diaria_racao = float(input())

qtd_final_racao = peso_total - (qtd_diaria_racao * 5)
print(f"{round(qtd_final_racao,2)}")
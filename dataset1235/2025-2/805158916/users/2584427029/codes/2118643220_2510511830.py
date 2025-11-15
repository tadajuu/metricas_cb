minutos_excedentes = int(input("Digite a quantidade de minutos: "))
plano = 45
custo_excedente = minutos_excedentes * 0.97
valor_total = plano + custos_excedente
valor_final = valor_total * 1.42
print(f"O valor da conta a pagar é: R${valor_final:.2f}")
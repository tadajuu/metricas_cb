n = float(input("Informe um numero: "))

porcentagem = n * (27/100)
porcentagem_arredondada = round(porcentagem,2)
print(porcentagem_arredondada)

valor_aumentado = n + (n * (42/100))
valor_aumentado_arredondado = round(valor_aumentado, 2)
print(valor_aumentado_arredondado)

valor_diminuido = n - (n * (63/100))
print(round(valor_diminuido,2))
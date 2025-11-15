n = float(input("Digite um numero: "))
porcentagem_em_27 = n * 0.27
porcentagem_em_27_arredondado = round(porcentagem_em_27, 2)

acrescimo_em_42 = n * 1.42
acrescimo_em_42_arredondado = round(acrescimo_em_42, 2)

desconto_em_63 = n * 0.37 # 100 - 63 = 37
desconto_em_63_arredondado = round (desconto_em_63, 2)

print(porcentagem_em_27_arredondado)
print(acrescimo_em_42_arredondado)
print(desconto_em_63_arredondado)
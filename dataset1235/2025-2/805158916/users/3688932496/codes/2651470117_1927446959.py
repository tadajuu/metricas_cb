#pegando o numero primeiro
X = float(input("Informe o valor do a pagar:"))
#tentado fazer dos 27% dos calculos agr:
porcentagem_27 = round(0.27 * X, 2)
#calculo dos 42% de acrescimo
acres_42 = round( X + (0.42 * X),2)
#CALCULO DOS 63% DE DESCONTO
desc_63 = round(X - (0.63 * X),2)
print("")
print(porcentagem_27 )
print(acres_42)
print(desc_63 )
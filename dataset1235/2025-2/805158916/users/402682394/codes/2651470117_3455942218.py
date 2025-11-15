Unit = float(input('Qual o valor de cada jogo? '))
Budget = float(input('Qual o seu orçamento? '))

Total = 8*Unit+45
Saldo = Budget-Total
print(round(Total, 2))
print(round(Saldo, 2))
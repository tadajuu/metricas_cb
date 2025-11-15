#Entrada
Quantidade_De_Praças = int(input("Digite a quantidade de praças de pedágio no caminho:"))
Taxa_De_Manutenção_Das_Estradas = float(20.00)
Valor_Do_Pedágio = Quantidade_De_Praças*9.80+Taxa_De_Manutenção_Das_Estradas
ICMS = (15/100)*Valor_Do_Pedágio
Custo_total = Valor_Do_Pedágio+ICMS
#Saída
print(round(Custo_total,2))

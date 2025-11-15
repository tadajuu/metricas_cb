#Entrada
Peso_Da_Ração = float(input("Digite o peso do saco de ração em gramas:"))
Quantidade_Diária_De_Ração = float(input("Digite a quantidade diária de ração"))
Quantidade_De_Ração_Restante = Peso_Da_Ração-Quantidade_Diária_De_Ração*5
#Saída
print(round(Peso_Da_Ração,2))
print(round(Quantidade_Diária_De_Ração,2))
print(round(Quantidade_De_Ração_Restante,2))

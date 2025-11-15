peso01 = 1
peso02 = 2
peso03 = 3
peso04 = 4

av1 = float(input("Digite a nota 1"))
av2 = float(input("Digite a nota 2"))
av3 = float(input("Digite a nota 3"))
av4 = float(input("Digite a nota 4"))

soma = (av1 * peso01) + (av2 * peso02) + (av3 * peso03) + (av4 * peso04)

soma_pesos = peso01 + peso02 + peso03 + peso04

media_ponderada = soma / soma_pesos
print(round(media_ponderada , 2))
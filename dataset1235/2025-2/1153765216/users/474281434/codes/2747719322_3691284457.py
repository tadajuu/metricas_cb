p1 = 1
p2 = 2
p3 = 3
p4 = 4

av1 = float(input("p1"))
av2 = float(input("p2"))
av3 = float(input("p3"))
av4 = float(input("p4"))
media_ponderada = (av1 * p1)+(av2 * p2)+(av3 * p3)+(av4 * p4)
soma = p1 + p2 + p3 + p4
media = media_ponderada / soma
print(round(media, 2)) 
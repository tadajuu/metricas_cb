n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media_ponderada = ((n1 * 1) + (n2 * 2) + (n3 * 3) + (n4 * 4))/10
media_ponderada_arredondamento = round(media_ponderada, 2)
print(media_ponderada_arredondamento)
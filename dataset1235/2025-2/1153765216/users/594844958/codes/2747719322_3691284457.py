notas = []

for i in range(4):
  nota = float(input())
  notas.append(nota)

media_ponderada = (notas[0] + (2*notas[1]) + (3*notas[2]) + (4*notas[3]))/10

print(round(media_ponderada, 2))